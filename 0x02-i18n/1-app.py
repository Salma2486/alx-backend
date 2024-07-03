#!/usr/bin/env python3
"""tdyh jtdyj tdy j"""
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """tdyh jtdyj tdy j"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@app.route('/')
def index():
    """tdyh jtdyj tdy j"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
