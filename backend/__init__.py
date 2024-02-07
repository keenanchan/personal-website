'''
backend/__init__.py

Entry point of the backend package.
'''

from flask import (
    Flask,
    send_from_directory
)
from flask_cors import CORS

# app = Flask(__name__)

# use this when frontend setup!
app = Flask(
    __name__,
    static_folder='../frontend/build',
    static_url_path=''
)

CORS(app)

from backend import routes