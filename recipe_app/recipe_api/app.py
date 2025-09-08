import sqlite3
import json
from flask import Flask, jsonify, request, g
from flask_cors import CORS

# This is a helper function to get a database connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('recipes.db')
        db.row_factory = sqlite3.Row
    return db

# This helper function closes the database connection when the request is over
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Initialize the Flask app
app = Flask(__name__)
# Enable CORS for all routes, allowing your React frontend to connect
CORS(app)

@app.teardown_appcontext
def teardown_db(exception):
    close_connection(exception)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Recipe API!"})

@app.route('/recipes', methods=['GET', 'POST'])
def handle_recipes():
    db = get_db()
    cursor = db.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM recipes ORDER BY id DESC")
        recipes = cursor.fetchall()
        # Convert fetched rows to a list of dictionaries
        recipes_list = []
        for recipe in recipes:
            recipe_dict = dict(recipe)
            # Deserialize the 'ingredients' JSON string back into a list
            recipe_dict['ingredients'] = json.loads(recipe_dict['ingredients'])
            recipes_list.append(recipe_dict)
        return jsonify(recipes_list)
    
    elif request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        ingredients = data.get('ingredients')
        instructions = data.get('instructions')

        if not title or not ingredients or not instructions:
            return jsonify({"error": "Missing data"}), 400

        # Serialize the ingredients list to a JSON string before storing
        ingredients_json = json.dumps(ingredients)

        cursor.execute(
            "INSERT INTO recipes (title, ingredients, instructions) VALUES (?, ?, ?)",
            (title, ingredients_json, instructions)
        )
        db.commit()
        
        return jsonify({
            "id": cursor.lastrowid,
            "title": title,
            "ingredients": ingredients,
            "instructions": instructions
        }), 201

@app.route('/recipes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_single_recipe(id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM recipes WHERE id = ?", (id,))
        recipe = cursor.fetchone()
        if not recipe:
            return jsonify({"error": "Recipe not found"}), 404
        
        recipe_dict = dict(recipe)
        # Deserialize the 'ingredients' JSON string back into a list
        recipe_dict['ingredients'] = json.loads(recipe_dict['ingredients'])
        return jsonify(recipe_dict)

    elif request.method == 'PUT':
        data = request.get_json()
        title = data.get('title')
        ingredients = data.get('ingredients')
        instructions = data.get('instructions')

        if not title or not ingredients or not instructions:
            return jsonify({"error": "Missing data"}), 400

        # Serialize the ingredients list to a JSON string
        ingredients_json = json.dumps(ingredients)

        cursor.execute(
            "UPDATE recipes SET title = ?, ingredients = ?, instructions = ? WHERE id = ?",
            (title, ingredients_json, instructions, id)
        )
        db.commit()

        cursor.execute("SELECT * FROM recipes WHERE id = ?", (id,))
        updated_recipe = cursor.fetchone()
        
        updated_recipe_dict = dict(updated_recipe)
        updated_recipe_dict['ingredients'] = json.loads(updated_recipe_dict['ingredients'])
        return jsonify(updated_recipe_dict)

    elif request.method == 'DELETE':
        cursor.execute("DELETE FROM recipes WHERE id = ?", (id,))
        db.commit()
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)

