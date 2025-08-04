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

@app.route('/spl', methods=['GET'])
def spl():
    return render_template('spl.html')

@app.route('/dmgen', methods=['GET'])
def dmgen():
    return render_template('dmgen.html')

@app.route('/ingestion', methods=['GET'])
def ingestion():
    return render_template('ingestion.html')

@app.route("/headers", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
def show_headers():
    headers = dict(request.headers)
    return jsonify(headers), 200



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)