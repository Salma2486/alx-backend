#!/usr/bin/env python3
"""tdyh jtdyj tdy j"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """tdyh jtdyj tdy j"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
