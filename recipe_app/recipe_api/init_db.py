import sqlite3
# Database name
DATABASE = 'recipes.db'

# Connect to the database
with sqlite3.connect(DATABASE) as conn:
    cursor = conn.cursor()


    create_table_sql = """
    CREATE TABLE IF NOT EXISTS recipes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        ingredients TEXT NOT NULL,
        instructions TEXT NOT NULL
    );
    """

    cursor.execute(create_table_sql)
    conn.commit()
print(f"Database '{DATABASE}' initialized with 'recipes' table.")