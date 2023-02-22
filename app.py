from flask import Flask, render_template
import json
import os
app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html',title='about')



@app.errorhandler(404)
def pageNotFound(e):
    return ("Page Does Not Exist")

if __name__ == "__main__":
    app.run(debug=True,port=8000)
