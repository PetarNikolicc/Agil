from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

def get_recipes_by_time(max_time):
    db_path = os.path.join(os.path.dirname(__file__), 'recipes.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT id, name, cooking_time FROM recipes WHERE cooking_time <= ?"
    cursor.execute(query, (max_time,))
    recipes = cursor.fetchall()
    conn.close()
    return recipes

def get_recipe_by_id(recipe_id):
    db_path = os.path.join(os.path.dirname(__file__), 'recipes.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = "SELECT name, description, instructions, image FROM recipes WHERE id = ?"
    cursor.execute(query, (recipe_id,))
    recipe = cursor.fetchone()
    conn.close()
    if recipe:
        return {'name': recipe[0], 'description': recipe[1], 'instructions': recipe[2], 'image': recipe[3]}
    else:
        return None

@app.route('/')
def homepage():
    time = request.args.get('time', 60)
    recipes = get_recipes_by_time(time)
    return render_template('index.html', recipes=recipes)

@app.route('/recipe/<int:recipe_id>')
def recipe_details(recipe_id):
    recipe = get_recipe_by_id(recipe_id)
    if recipe:
        return jsonify(recipe)
    else:
        return jsonify({'error': 'Recipe not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
