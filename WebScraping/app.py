from flask import Flask, render_template, redirect, jsonify
import pymongo
from scrapmars import scrape_all
app = Flask(__name__)

conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient(conn)

db = client.mars_db

@app.route('/')
def index():
  
    mars = db.mars_table.find_one()
    print(mars)

    return render_template('index.html', mars=mars)

@app.route('/scrape')
def scrape():
    scrape_data = scrape_all()
    db.mars_table.update({},scrape_data,upsert=True)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

    