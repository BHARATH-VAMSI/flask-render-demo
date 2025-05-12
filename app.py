from flask import Flask, render_template, abort
import json

app = Flask(__name__)

with open("mobiles.json") as f:
    mobiles = json.load(f)

@app.route("/")
def index():
    return render_template("index.html", mobiles=mobiles)

@app.route("/category/<int:price>")
def category(price):
    filtered = [m for m in mobiles if m["price"] <= price]
    return render_template("category.html", mobiles=filtered, price=price)

@app.route("/mobile/<id>")
def mobile_detail(id):
    mobile = next((m for m in mobiles if m["id"] == id), None)
    if not mobile:
        abort(404)
    return render_template("mobile_detail.html", mobile=mobile)

@app.route("/brand/<brand_name>")
def brand(brand_name):
    filtered = [m for m in mobiles if m["brand"].lower() == brand_name.lower()]
    return render_template("brand.html", mobiles=filtered, brand=brand_name.capitalize())
