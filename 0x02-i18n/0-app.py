#!/usr/bin/env python3
"""
0-app.py - Basic Flask App
"""

from flask import Flask, render_template
from typing import Any

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> Any:
    """
    Render the index.html template.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
