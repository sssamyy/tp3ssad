from flask import render_template
from . import app  # Import the app from __init__.py

@app.route('/totp')
def totp():
    return render_template('totp.html')