from flask import Flask
app = Flask(__name__)
from flask import render_template
from config import  app
@app.route("/")
def index():
    