from flask import Flask, render_template
# import seaborn as sns
# import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")