# __init__.py

from flask import Flask

# Initialize the app
app = Flask(__name__)
app.config['SECRET_KEY'] = '7d3e1c8f534ef24b9a8698b8d7b6e8551835c17949bc6d4e2219b080a0d7cf29'  # Secret key for session and CSRF protection

# Import routes after app initialization
from .auth_methods import *  # Import routes from auth_methods.py
from .totp import *  # Import routes from totp_methods.py

# Start the app if this file is run directly
if __name__ == "__main__":
    app.run(debug=True)
