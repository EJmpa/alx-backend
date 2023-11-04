#!/usr/bin/env python3
"""
This module defines a basic Flask app.
"""

from flask import Flask, render_template
from flask_babel import Babel
from typing import List

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    This class defines the configuration for the Flask app.
    """
    LANGUAGES: List[str] = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    Renders the index.html template.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
