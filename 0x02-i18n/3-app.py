#!/usr/bin/env python3
"""
3-app.py - Babel Configuration
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Any

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    This class defines the configuration for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)

babel.init_app(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching language from the user's request.
    """
    supported_languages = app.config['LANGUAGES']
    return request.accept_languages.best_match(supported_languages)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> Any:
    """
    Renders the index.html template.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
