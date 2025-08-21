import sqlite3


DATABASE = 'tasks.db'


# connect to the database
with sqlite3.connect(DATABASE) as conn:

    # create a cursor object which allows us to execute SQL commands
    cursor = conn.cursor()

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        completed BOOLEAN DEFAULT 0
    );

    """
    # Execute the SQL command to create the table
    cursor.execute(create_table_sql)
    conn.commit()

# print a conformation message once the script finishes.
print(f"Database '{DATABASE}' and table 'tasks' initialized successfully")