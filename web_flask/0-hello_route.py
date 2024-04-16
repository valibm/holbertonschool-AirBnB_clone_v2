#!/usr/bin/python3
"""Is a scripts that starts a simple flask web application"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Prints Hello HBNB!"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
