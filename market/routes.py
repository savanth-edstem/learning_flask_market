from market import app
from flask import render_template
from market.models import Item


@app.route('/')
def hello_world():
    return "<h1>Hello world...</h1>"


@app.route('/home')
@app.route("/home2")
def home_page():
    return render_template("home.html")


@app.route('/about/<username>')  # dynamic route
def about_page(username):
    return f"<h1>This is about page of {username}</h>"


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)
