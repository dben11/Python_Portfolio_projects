from flask import Flask, jsonify
import json
import random

app = Flask(__name__)


quotes_data = []

def load_quotes():
    global quotes_data
    try:
        with open('quotes.json', 'r') as file:
            quotes_data = json.load(file)
        print("Quotes loaded successfully from quotes.json")
    except FileNotFoundError:
        print("Error: quotes.json not found . Please create the file .")
    except json.JSONDecodeError:
        print("Error: Could not decode quotes.json (invalid JSON format).")
        quotes_data = []

    except Exception as e:
        print(f"An unexpected error occurred while loading quotes: {e}")
        quotes_data =[]

# Defining the routes
@app.route('/')
def home():
    return "Welcome to the Quote of the Day API! Visit /quote to get a random quote!!!"

@app.route('/quote', methods=['GET', 'POST'])
def get_random_quote():
    
    if not quotes_data:
        return jsonify({"error": "No quotes available. check quotes.json"}), 500
    random_quote = random.choice(quotes_data)
    return jsonify(random_quote)


if __name__ == '__main__':
    load_quotes()
    app.run(debug=True)