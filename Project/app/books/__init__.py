from flask import Blueprint

book_routes = Blueprint("books", __name__, url_prefix='/books', static_folder='static', template_folder='templates')
from app.books.books import *