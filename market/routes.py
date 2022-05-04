from market import app
from flask import render_template
from market.models import Item
from market.forms import RegisterForm


# @app.route('/')
# def hello_world():
#     return "<h1>Hello world...</h1>"


@app.route('/')
@app.route("/home")
def home_page():
    return render_template("home.html")


# this is a dynamic route
# @app.route('/about/<username>')
# def about_page(username):
#     return f"<h1>This is about page of {username}</h>"


@app.route('/market')
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)


@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('register.html', form=form)
