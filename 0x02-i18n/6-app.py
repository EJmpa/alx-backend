#!/usr/bin/env python3
"""
6-app.py - Babel Configuration
"""

from flask import Flask, render_template, request, g
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


def get_user():
    """gets user dictionary from user table based on url param"""
    user_id = request.args.get('login_as')
    if user_id:
        user_id = int(user_id)
    return users.get(user_id)


@app.before_request
def before_request():
    """sets user as global variable"""
    g.user = get_user()


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

    # Locale from URL parameters
    forced_locale: str = request.args.get('locale')
    if forced_locale and forced_locale in supported_languages:
        return forced_locale

    # Locale from user settings
    if g.user and 'locale' in g.user and g.user['locale'] in supported_languages:
        return g.user['locale']

    # Locale from request header
    header_locale: str = request.headers.get('Accept-Language')
    if header_locale:
        header_locale = header_locale.split(',')[0]
        for lang in header_locale.split(';')[0].split(','):
            if lang in supported_languages:
                return lang

    # Default locale
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    Renders the index.html template with translated text.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
