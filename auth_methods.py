# auth_methods.py

from flask import render_template, request, redirect, url_for, flash
from . import app  # Import the app from __init__.py

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # Simple login logic
        if email == "user@example.com" and password == "password":
            flash('Login successful!', 'success')
            return redirect(url_for('home'))  # Use 'home' directly without blueprint prefix
        else:
            flash('Invalid credentials!', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))  # Use 'login' directly without blueprint prefix
    return render_template('register.html')
