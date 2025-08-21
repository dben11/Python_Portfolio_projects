from tarfile import BLOCKSIZE
from flask import Flask, request, jsonify
import sqlite3


# Initialize the flask application
app = Flask(__name__)

# define the path to your
DATABASE = 'tasks.db'

# _____Database helper functions______

def get_db_connection():
    """
    Establishes a connection to the SQLite database
    It will create the database file if it doesn't exist.

    """
    # Connect to the database file
    conn = sqlite3.connect(DATABASE)

    # Set the row_factory to sqlite3.Row
    conn.row_factory = sqlite3.Row
    return conn

def close_db_connection(exception=None):
    """
    Close the database connection at the end of a request
    This function is registered with Flasks teardown_appcontext.
    """
    db = getattr(app, '_database', None)
    if db is not None:
        db.close()

app.teardown_appcontext(close_db_connection)


# Define the root route
@app.route('/')
def home():
    return 'Welcome to the TO-DO List API! Use endpoints like /tasks.'

# Endpoint to get all tasks
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    conn = get_db_connection()
    # Convert the list of sqlite3.Row objects into a list of dictionaries
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    # Check if the task exists
    if task is None: # type: ignore
        return jsonify({"error": "Task not found"}), 404
    task_dict = dict(task) # type: ignore
    # Return the list of tasks as a JSON responds
    return jsonify(task_dict)



#NEW: Endpoint to add a new task (POST method)
@app.route('/tasks', methods=['POST'])
def add_task():
    print(f"Incoming request headers: {request.headers}")
    print(f"Incoming JSON data received by get_json(): {request.get_json()}")
    new_task_data = request.get_json()
    if  not new_task_data or 'description' not in new_task_data:
        return jsonify({"error": "Description is required"}), 400
    
    description = new_task_data['description']
    completed = new_task_data.get('completed', False)

    conn = get_db_connection()
    try:
        cursor = conn.execute(
            'INSERT INTO tasks (description, completed) VALUES (?, ?)',
            (description, completed)
        
        )
        conn.commit()
        # Get the id of the newly created task
        new_task_id = cursor.lastrowid
        created_task = conn.execute(
            'SELECT * FROM tasks WHERE id = ?', (new_task_id,)).fetchone()
        

        # return the newly created task as a JSON response with a 201 status code
        return jsonify(dict(created_task)), 201
    except sqlite3.IntegrityError as e:
        return jsonify({"error": f"Database integrity error: {e}"}), 500
    except Exception as e:
        conn.rollback()
        return jsonify({"error": f"An error occurred: {e}"}), 500
    

# New: Endpoint to update an existing task by ID (PUT method)
# app.py

# ... (existing imports and other functions) ...

# Endpoint to update an existing task by ID (PUT method).
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    updated_data = request.get_json()

    if not updated_data:
        return jsonify({"error": "No data provided for update"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    set_clauses = []
    parameters = []

    if 'description' in updated_data:
        set_clauses.append("description = ?")
        parameters.append(updated_data['description'])
    
    if 'completed' in updated_data:
        set_clauses.append("completed = ?")
        parameters.append(1 if updated_data['completed'] else 0)

    # This check is crucial: If no valid fields were provided, return an error.
    if not set_clauses:
        return jsonify({"error": "No valid fields to update (e.g., 'description' or 'completed')"}), 400

    # Add the task_id to the parameters for the WHERE clause.
    parameters.append(task_id)

    # Construct the full SQL UPDATE statement.
    update_sql = f"UPDATE tasks SET {', '.join(set_clauses)} WHERE id = ?"
    
    try:
        cursor.execute(update_sql, tuple(parameters))
        conn.commit()

        # Check if any row was actually updated.
        if cursor.rowcount == 0:
            return jsonify({"error": "Task not found"}), 404
        
        # Retrieve the updated task from the database to return its latest state.
        updated_task = conn.execute(
            'SELECT * FROM tasks WHERE id = ?', (task_id,)
        ).fetchone()

        # Ensure updated_task is not None after fetchone (defensive check)
        if updated_task is None:
            # This case is highly unlikely if rowcount > 0, but good for robustness
            return jsonify({"error": "Failed to retrieve updated task"}), 500

        # Return the updated task as JSON. This is the crucial return statement.
        return jsonify(dict(updated_task)) # This must be reached if update is successful

    except sqlite3.IntegrityError as e:
        conn.rollback()
        return jsonify({"error": f"Database integrity error: {e}"}), 500
    except Exception as e:
        conn.rollback()
        return jsonify({"error": f"An error occurred: {e}"}), 500

# ... (existing if __name__ == '__main__': block) ...


# New: Endpoint to delete a task by ID (DELETE method).
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        conn.commit()

        # Check if any row actually deleted.
        if cursor.rowcount == 0:
            return jsonify({"error": "Task not found"}), 404
        return '', 204
    
    except Exception as e:
        # Catch any unexpected errors during th database operation.
        conn.rollback()
        return jsonify({"error": f"An error occurred: {e}"}), 500
# ... (existing if __name__ == '__main__': block) ...
        





















if __name__ == '__main__':
    app.run(debug=True)


