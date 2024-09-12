from app.auth import auth_routes
from app.models import User,Book
from flask import render_template, request, redirect, url_for,session,flash
from app.books import book_routes 


# Add Book
@book_routes.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if 'user_id' in session.keys():
        if request.method == 'POST':
            title = request.form['title']
            image = request.files['image'].read()  # Store image as BLOB
            data = {'title':title, 'image':image, 'user_id':session['user_id']}
            Book.addBook(data)
            return redirect(url_for('books.view_books'))
        return render_template('add_book.html')
    return redirect(url_for('auth.login'))


# View Books
@book_routes.route('/book')
def view_books():
    if 'user_id' in session.keys():
        user = User.query.get(session['user_id'])
        books = user.books
        return render_template('view_books.html', books=books)
    return redirect(url_for('auth.login'))



# Delete Book
@book_routes.route('/delete_book/<int:book_id>')
def delete_book(book_id):
    Book.deleteBook(book_id)
    return redirect(url_for('books.view_books'))

# Admin Dashboard
@book_routes.route('/admin_dashboard')
def admin_dashboard():
    if not session.get('is_admin'):
        return "Access Denied!"
    users = User.query.all()
    books = Book.query.all()
    return render_template('admin_dashboard.html', users=users, books=books)

    
@book_routes.route("error")
def get_worng_info():
    return render_template("error.html")