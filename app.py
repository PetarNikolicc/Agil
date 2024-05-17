from flask import Flask, render_template, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
import os
import pandas as pd


app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'Database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Recipes(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    minutes = Column(String)
    n_steps	= Column(String)
    steps = Column(String)
    ingredients	= Column(String)
    n_ingredients = Column(String)

with app.app_context():
    db.drop_all()
    db.create_all()
    file = os.path.join(basedir, "data2.csv")
    df = pd.read_csv(file)

    for index, row in df.iterrows():
        recipe = Recipes(
            name = row["name"],
            minutes = row["minutes"],
            n_steps = row["n_steps"],
            steps = row["steps"],
            ingredients = row["ingredients"],
            n_ingredients = row["n_ingredients"]
        )
        db.session.add(recipe)
    db.session.commit()


@app.route("/")
def homepage():
    recipes = Recipes.query.all()
    return render_template("index.html", recipes=recipes)





# @app.route("/all_recipes", methods=["GET"])
# def all_recipes():
#     page = request.args.get('page', 1, type=int)
#     per_page = 30 # Antal recept som visas per sida
#     get_recipes = request.args.get("get_recipes", "")
#     sort_column_id = request.args.get("sort_column_id", "minutes")
#     sort_by_order = request.args.get("sort_by_order", "desc")
    
#     recipes = User.query.filter(
#         User.name.like("%" + get_users + "%") |
#         User.age.like("%" + get_users + "%") |
#         User.phone.like("%" + get_users + "%") |
#         User.country.like("%" + get_users + "%")
#     )
    
#     if sort_column_id == 'minutes':
#         sort_by_order = User.name
#     elif sort_column_id == 'age':
#         sort_by_order = User.age
#     elif sort_column_id == 'phone':
#         sort_by_order = User.phone
#     elif sort_column_id == 'country':
#         sort_by_order = User.country
#     else:
#         sort_by_order = User.id

#     if sort_by_order == 'asc':
#         users = users.order_by(sort_by_order.asc())
#     elif sort_by_order == 'desc':
#         users = users.order_by(sort_by_order.desc())

#     users = users.paginate(page=page, per_page=per_page)

#     num_pages = (users.total +  per_page - 1) // per_page
    
#     return render_template(
#         "all_users.html",
#         page=page,
#         get_users=get_users,
#         num_pages=num_pages,
#         users=users, 
#         sort_by_order=sort_by_order,
#         sort_column_id=sort_column_id
#         )