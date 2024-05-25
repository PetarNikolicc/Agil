from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

DATABASE = 'recipes.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def get_recipes_by_time(time):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT name, cooking_time, image_path, instructions FROM recipes WHERE cooking_time = ?", (time,))
    recipes = cursor.fetchall()
    return recipes

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/time', methods=['GET'])
def time():
    try:
        time = request.args.get('time')
        if time:
            recipes = get_recipes_by_time(int(time))
        else:
            recipes = []
        return render_template('time.html', recipes=recipes)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
