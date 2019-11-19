from flask import Flask, jsonify, render_template, request, redirect
from flask_pymongo import PyMongo
import scrape_mars




app = Flask(__name__)





conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)





@app.route("/")
def index():


if __name__ == "__main__":
    app.run(debug=True)