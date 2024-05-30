from flask import Flask, render_template, render_template, request, redirect, url_for, jsonify
import sqlite3
import os
import pandas as pd

app = Flask(__name__)

def get_recipes_by_time(exact_time):
    db_path = os.path.join(os.path.dirname(__file__), 'recipes.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes WHERE cooking_time = ?", (exact_time,))
    recipes = cursor.fetchall()
    conn.close()
    return recipes

@app.route('/')
def homepage():
    time = request.args.get('time')
    if time:
        try:
            time = int(time)
            recipes = get_recipes_by_time(time)
        except ValueError:
            recipes = []
    else:
        recipes = []
    return render_template('index.html', recipes=recipes)



if __name__ == '__main__':
    app.run(debug=True)