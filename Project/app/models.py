from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from werkzeug.security import generate_password_hash, check_password_hash
# step-1: ORM
db = SQLAlchemy()



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    books = db.relationship('Book', backref='owner', lazy="select")

    def __init__(self, username, password, is_admin=False):
        self.username = username
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    @classmethod
    def addUser(cls,data):
        new_user = cls(username=data['username'], password=data['password'])
        db.session.add(new_user)
        db.session.commit()

    @classmethod
    def deleteUser(cls,user_id):
        user = cls.query.get(user_id)
        db.session.delete(user)
        db.session.commit()




class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    image = db.Column(db.LargeBinary)  # Store images as BLOBs
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __init__(self, title, image=None, user_id=None):
        self.title = title
        self.image = image
        self.user_id = user_id

    @classmethod
    def addBook(cls,data):
        title=data['title']
        image=data['image']
        user_id=data['user_id']

        new_book = cls(title=title, image=image, user_id=user_id)
        db.session.add(new_book)
        db.session.commit()

    @classmethod
    def deleteBook(cls,book_id):
        book = cls.query.get(book_id)
        db.session.delete(book)
        db.session.commit()
