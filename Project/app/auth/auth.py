# signup, login, authntication, authorization,logout

from app.auth import auth_routes
from flask import render_template, request, redirect, url_for,session,flash
from werkzeug.security import check_password_hash
from app.models import User



# User Registration
@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return "Username already exists!"
        data={'username':username, 'password':password}
        User.addUser(data)
        return redirect(url_for('auth.login'))
    return render_template('register.html')

# User Login
@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['is_admin'] = user.is_admin
            return redirect(url_for('books.view_books'))
        return "Invalid credentials!"
    return render_template('login.html')

# Logout
@auth_routes.route('/logout')
def logout():
    if 'user_id' in session.keys():
        session.pop('user_id')
        session.pop('is_admin')
    return redirect(url_for('auth.login'))



# Delete User
@auth_routes.route('/delete_user/<int:user_id>')
def delete_user(user_id):
    if not session.get('is_admin'):
        return "Access Denied!"
    User.deleteUser(user_id)
    return redirect(url_for('books.admin_dashboard'))
