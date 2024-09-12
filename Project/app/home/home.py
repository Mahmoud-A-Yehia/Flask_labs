from app.home import home_routes
from flask import render_template

@home_routes.route('/')
def welcome_page():
    print("Hello")
    return render_template("home.html")