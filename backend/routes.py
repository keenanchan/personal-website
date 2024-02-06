from flask import (
    request,
    send_from_directory
)
from backend import app

@app.route("/")
def index():
    # return "Hello! I'm Keenan, welcome to my personal website."
    
    # use when frontend setup!
    return send_from_directory(
        app.static_folder,
        'index.html'
    )

# TODO: use blueprints for API
@app.route("/api/hello")
def hello():
    return {
        'resultStatus': 'SUCCESS',
        'message': '/api/hello! This is Keenan.'
    }
