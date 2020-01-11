from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/mars"

mongo = PyMongo(app)
@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars = mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars_scrape = scrape_mars.news()
    mars_scrape = scrape_mars.nasa_image()
    mars_scrape = scrape_mars.weather()
    mars_scrape = scrape_mars.mars_facts()
    mars_scrape = scrape_mars.hemispheres()
    
    mars.update({}, mars_scrape, upsert=True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)