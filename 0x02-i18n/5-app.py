#!/usr/bin/env python3
"""
5-app.py - Babel Configuration
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import List

app: Flask = Flask(__name__)
babel: Babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    return users.get(user_id)


@app.before_request
def before_request():
    user_id = request.args.get("login_as")
    g.user = get_user(int(user_id)) if user_id else None


class Config:
    """
    This class defines the configuration for the Flask app.
    """
    LANGUAGES: List[str] = ["en", "fr"]
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)
babel.init_app(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determine the best-matching language from the user's
    request, or use the forced locale.
    """
    supported_languages: List[str] = app.config['LANGUAGES']
    forced_locale: str = request.args.get('locale')

    if forced_locale and forced_locale in supported_languages:
        return forced_locale
    else:
        return request.accept_languages.best_match(supported_languages)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    Renders the index.html template with translated text.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
