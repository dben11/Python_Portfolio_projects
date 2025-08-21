# Project: TO-DO List API

This is a RESTFUL API built with Python and flask that allows users to manage their to-do list items programmatically. It provides standard CRUD(Create, Read, Update, Delete) operations, storing tasks persistently in a SQLite database. This project demonstrates foundational backend development concepts, including API design, database interaction, and handling HTTP requests and response.

## Features

This API supports the following core functionalities for managing to-do tasks:

- **Create Task:** Add new to-do items to the list.
  - `POST /tasks`
- **Request Body Example:** `{"description": "Learn Flask APIs", "Completed": false}`
- **Get All Tasks:** Retrieve a list of all existing to-do items.
  - `GET /tasks`
- **Get Single Task:** Retrieve details for a specific to-do items by its unique ID.
  - `GET /tasks/<id>` (e.g., `/tasks/1`)
- **Update Task:** Modify the description or completion status of an existing to-do item
  - `PUT /tasks/<id>` (e.g. `/tasks/1`)
- **Request Body Example:** `{"description": "Master Flask APIs", "completed": true}` (supports partial updates)
- **Delete Task:** Remove a to-do item from the list.
  - `DELETE /tasks/<id>` (e.g., `/tasks/1`)

## Technologies Used

The To-Do List API is built using the following technologies:

- **Python 3:** The core programming language.
- **Flask:** A lightweight Python web framework used for building the API endpoints.
- **SQLite3:** A C-library that provides a lightweight, file-based SQL database, used for persistent storage of tasks.
- **`sqlite3` (Python module):** The built-in Python module for interacting with SQLite databases.
- **`curl` or Postman/Insomnia:** (Optional, for testing) Command-line tool or GUI applications used for sending HTTP requests to test the API endpoints.

## Setup and Running

Follow these steps to set up and run the To-Do List API locally.

### Prerequisites

- **Python 3.8+** installed on your system.
- **`pip`** (Python package installer) installed.

### Installation

1.  **Clone the repository (or create the project directory):**
    If you're getting this code from a repository:

    ```bash
    git clone [https://github.com/your-username/todo-list-api.git](https://github.com/your-username/todo-list-api.git)
    cd todo-list-api
    ```

    If you're setting it up as a new local project:

    ```bash
    mkdir todo_api
    cd todo_api
    ```

2.  **Create and activate a virtual environment:**
    It's highly recommended to use a virtual environment to manage project dependencies.

    - **Create:**
      ```bash
      python -m venv venv
      ```
    - **Activate:**
      _ On macOS/Linux:
      `bash
        source venv/bin/activate
        `
      _ On Windows:
      `bash
        .\venv\Scripts\activate
        `
      (You should see `(venv)` at the beginning of your terminal prompt once activated.)

3.  **Install dependencies:**
    With your virtual environment activated, install Flask.
    ```bash
    pip install Flask
    ```

### Database Initialization

The API uses a SQLite database (`tasks.db`) for persistent storage. You need to initialize it once to create the `tasks` table.

1.  **Create `init_db.py`:**
    Make sure you have the `init_db.py` file in your project directory with the following content:

    ```python
    # init_db.py
    import sqlite3

    DATABASE = 'tasks.db'

    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            description TEXT NOT NULL,
            completed BOOLEAN DEFAULT 0
        );
        """
        cursor.execute(create_table_sql)
        conn.commit()

    print(f"Database '{DATABASE}' and table 'tasks' initialized successfully.")
    ```

2.  **Run the initialization script:**
    ```bash
    python init_db.py
    ```
    You should see the message: `Database 'tasks.db' and table 'tasks' initialized successfully.` And a `tasks.db` file will appear in your directory.

### Running the API

1.  **Create `app.py`:**
    Ensure you have your main Flask application file (`app.py`) in the project directory, containing all the API endpoint code we've developed (including `GET /tasks`, `POST /tasks`, `GET /tasks/<id>`, `PUT /tasks/<id>`, and `DELETE /tasks/<id>`).

2.  **Start the Flask development server:**
    With your virtual environment still activated:
    ```bash
    python app.py
    ```
    The API will typically run on `http://127.0.0.1:5000/`. You will see messages in your terminal indicating the server is running.

## API Usage

Once the API is running (typically on `http://127.0.0.1:5000/`), you can interact with it using tools like `curl` (command-line) or graphical clients like Postman/Insomnia.

### 1. Get All Tasks

Retrieves a list of all to-do items.

- **Endpoint:** `GET /tasks`
- **Curl Command:**
  ```bash
  curl [http://127.0.0.1:5000/tasks](http://127.0.0.1:5000/tasks)
  ```
- **Example Response:**
  ```json
  [
    {
      "completed": 0,
      "description": "Learn Flask APIs",
      "id": 1
    },
    {
      "completed": 1,
      "description": "Buy groceries",
      "id": 2
    }
  ]
  ```

### 2. Add a New Task

Adds a new to-do item to the list. The `description` is required. `completed` is optional (defaults to `false`).

- **Endpoint:** `POST /tasks`
- **Curl Command:**
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"description": "Write API documentation", "completed": false}' [http://127.0.0.1:5000/tasks](http://127.0.0.1:5000/tasks)
  ```
- **Example Response:**
  ```json
  {
    "completed": 0,
    "description": "Write API documentation",
    "id": 3
  }
  ```

### 3. Get a Single Task

Retrieves details for a specific to-do item by its unique ID.

- **Endpoint:** `GET /tasks/<id>`
- **Curl Command:** (Using an example ID of `1`)
  ```bash
  curl [http://127.0.0.1:5000/tasks/1](http://127.0.0.1:5000/tasks/1)
  ```
- **Example Response:**
  ```json
  {
    "completed": 0,
    "description": "Learn Flask APIs",
    "id": 1
  }
  ```
- **Error Response (Task Not Found):**
  ```json
  {
    "error": "Task not found"
  }
  ```
  (HTTP Status: 404 Not Found)

### 4. Update a Task

Modifies the description or completion status of an existing to-do item. Supports partial updates (you only need to send the fields you want to change).

- **Endpoint:** `PUT /tasks/<id>`
- **Curl Command (Update Description):** (Using an example ID of `1`)
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"description": "Master Flask API development"}' [http://127.0.0.1:5000/tasks/1](http://127.0.0.1:5000/tasks/1)
  ```
- **Curl Command (Mark as Completed):** (Using an example ID of `1`)
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"completed": true}' [http://127.0.0.1:5000/tasks/1](http://127.0.0.1:5000/tasks/1)
  ```
- **Example Response (After update):**
  ```json
  {
    "completed": 1,
    "description": "Master Flask API development",
    "id": 1
  }
  ```
- **Error Response (Task Not Found):**
  ```json
  {
    "error": "Task not found"
  }
  ```
  (HTTP Status: 404 Not Found)

### 5. Delete a Task

Removes a to-do item from the list.

- **Endpoint:** `DELETE /tasks/<id>`
- **Curl Command:** (Using an example ID of `1`)
  ```bash
  curl -X DELETE [http://127.0.0.1:5000/tasks/1](http://127.0.0.1:5000/tasks/1)
  ```
- **Example Response:** (Successful deletion will return no content)
  - No response body (HTTP Status: 204 No Content)
- **Error Response (Task Not Found):**
  ```json
  {
    "error": "Task not found"
  }
  ```
  (HTTP Status: 404 Not Found)

## Error Handling

The API provides clear, descriptive error messages with appropriate HTTP status codes to help clients understand what went wrong.

- **400 Bad Request:**

  - Returned when the client sends an invalid request, such as missing required data in the request body (e.g., `description` when adding a task), or providing data in an incorrect format.
  - **Example Response:**
    ```json
    {
      "error": "Description is required"
    }
    ```

- **404 Not Found:**

  - Returned when a client requests a resource (task) that does not exist for the given ID.
  - **Example Response:**
    ```json
    {
      "error": "Task not found"
    }
    ```

- **500 Internal Server Error:**
  - Returned for unexpected server-side issues or database errors that prevent the API from fulfilling the request.
  - **Example Response:**
    ```json
    {
      "error": "An error occurred: [specific error message]"
    }
    ```

## Project Structure

The project directory is structured as follows:

todo_api/
├── venv/ # Python virtual environment (contains installed dependencies)
├── app.py # The main Flask application with all API endpoints
├── init_db.py # Script to initialize the SQLite database and create the 'tasks' table
└── tasks.db # SQLite database file (created after running init_db.py)
└── README.md # This README file

- **`venv/`**: Contains the isolated Python environment and all project dependencies.
- **`app.py`**: The core of the API, where Flask routes are defined and database interactions for CRUD operations are handled.
- **`init_db.py`**: A utility script used once to set up the `tasks.db` file and the necessary `tasks` table.
- **`tasks.db`**: The SQLite database file where all to-do tasks are persistently stored.
- **`README.md`**: Project documentation, providing setup, usage, and other details.

## Key Learnings

This project provided hands-on experience and reinforced understanding of several key backend development concepts:

- **RESTful API Design Principles:** Implemented standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) and structured URLs (`/tasks`, `/tasks/<id>`) to create a clear and intuitive API.
- **Flask Web Framework:** Gained practical experience in setting up Flask applications, defining routes, handling requests, and returning JSON responses.
- **Database Integration (SQLite3):** Learned how to connect a Python application to a relational database using `sqlite3`, execute SQL queries (`SELECT`, `INSERT`, `UPDATE`, `DELETE`), and manage database connections.
- **SQL Fundamentals:** Applied basic SQL commands for table creation and CRUD operations.
- **Data Persistence:** Understood how to store and retrieve application data reliably using a database, ensuring data is not lost when the application stops.
- **JSON Handling:** Worked with parsing incoming JSON request bodies (`request.get_json()`) and serializing Python dictionaries to JSON responses (`jsonify()`).
- **Error Handling & HTTP Status Codes:** Implemented `try-except` blocks for robustness and used appropriate HTTP status codes (e.g., `200 OK`, `201 Created`, `400 Bad Request`, `404 Not Found`, `500 Internal Server Error`) to provide clear feedback to clients.
- **Virtual Environments:** Best practices for managing project dependencies using `venv`.

## Future Enhancements

This API provides a solid foundation for managing tasks. Here are some ideas for future enhancements:

- **User Authentication:** Implement user registration and login, allowing each user to manage their own private list of tasks. This would involve adding a user management system and securing API endpoints.
- **Filtering and Pagination:**
  - Add query parameters to the `GET /tasks` endpoint to allow filtering tasks (e.g., `GET /tasks?completed=true` to get only completed tasks).
  - Implement pagination to handle large numbers of tasks efficiently (e.g., `GET /tasks?page=1&limit=10`).
- **Task Prioritization:** Add a `priority` field to tasks (e e.g., "high", "medium", "low") and endpoints to update/filter by priority.
- **Due Dates:** Include a `due_date` field for tasks, allowing users to set and manage deadlines.
- **Search Functionality:** Add a search endpoint (e.g., `GET /tasks/search?query=keyword`) to find tasks based on keywords in their description.
- **Testing Suite:** Implement unit and integration tests using frameworks like `pytest` to ensure the API's reliability and prevent regressions.
- **Deployment:** Deploy the Flask API to a cloud platform (e.g., Heroku, Render, AWS, Google Cloud) so it's accessible publicly.
