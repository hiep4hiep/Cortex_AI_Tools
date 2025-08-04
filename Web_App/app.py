from flask import Flask, render_template, request
import markdown
from dotenv import load_dotenv
from flask import jsonify
import sys
import os

load_dotenv()  # Load from .env if exists


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', response="", loading=False)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)