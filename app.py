from flask import Flask, render_template, render_template, request, redirect, url_for, jsonify
import sqlite3
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, String, Text
import os
import pandas as pd

app = Flask(__name__)

# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# class Recipes(db.Model):
#     id = Column(Integer, primary_key=True)
#     name = Column(Text)
#     minutes = Column(String)
#     n_steps	= Column(String)
#     steps = Column(String)
#     ingredients	= Column(String)
#     n_ingredients = Column(String)

# with app.app_context():
#     db.drop_all()
#     db.create_all()
#     file = os.path.join(basedir, "data2.csv")
#     df = pd.read_csv(file)

#     for index, row in df.iterrows():
#         recipe = Recipes(
#             name = row["name"],
#             minutes = row["minutes"],
#             n_steps = row["n_steps"],
#             steps = row["steps"],
#             ingredients = row["ingredients"],
#             n_ingredients = row["n_ingredients"]
#         )
#         db.session.add(recipe)
#     db.session.commit()

def get_recipes_by_time(max_time):
    db_path = os.path.join(os.path.dirname(__file__), 'recipes.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM recipes WHERE cooking_time <= ?", (max_time,))
    recipes = cursor.fetchall()
    conn.close()
    return recipes

@app.route('/')
def homepage():
    time = request.args.get('time')
    if time:
        recipes = get_recipes_by_time(time)
    else:
        recipes = get_recipes_by_time(60)  # Default to 60 minutes or you can choose to show all or none
    return render_template('index.html', recipes=recipes)

@app.route('/filter', methods=['GET'])
def filter_recipes():
    max_time = request.args.get('time')
    recipes = get_recipes_by_time(max_time)
    return jsonify(recipes)

if __name__ == '__main__':
    app.run(debug=True)