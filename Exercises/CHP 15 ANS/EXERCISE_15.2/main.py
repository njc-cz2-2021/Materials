from flask import Flask, render_template, request
from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["jp_mobile"]
coll = db["Phones"]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        brand = request.form['brand']
        results = list(coll.find({'brand': brand}))
        return render_template('results.html', info=results, brand_name=results["brand"])
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()