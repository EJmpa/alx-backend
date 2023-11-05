#!/usr/bin/env python3
"""
app.py - Babel Configuration
"""

from pytz import timezone, exceptions as pytz_exceptions
from flask import Flask, render_template, request, g
from flask_babel import Babel
from datetime import datetime
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


@babel.timezoneselector
def get_timezone() -> str:
    """Determine the best-matching time zone for the user."""
    # Find the timezone parameter in URL parameters
    timezone_param = request.args.get('timezone')

    if timezone_param:
        try:
            # Validate that the provided timezone is a valid time zone
            timezone(timezone_param)
            return timezone_param
        except pytz_exceptions.UnknownTimeZoneError:
            pass

    # Find the time zone from user settings
    if g.user:
        user_timezone = g.user.get('timezone')
        if user_timezone:
            try:
                # Validate that the user's preferred timezone is valid
                timezone(user_timezone)
                return user_timezone
            except pytz_exceptions.UnknownTimeZoneError:
                pass

    # Default to UTC if no valid timezone found
    return Config.BABEL_DEFAULT_TIMEZONE


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
    if g.user and 'locale' in g.user and \
            g.user['locale'] in supported_languages:
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
    # Get the current time in the inferred time zone
    user_timezone = get_timezone()
    current_time = datetime.now(
            timezone(user_timezone)
            ).strftime('%b %d, %Y, %I:%M:%S %p')
    return render_template('index.html', current_time=current_time)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
