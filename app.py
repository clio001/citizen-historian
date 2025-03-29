from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)

@app.route('/')
def index():
    with open('static/db/docs.json', 'r', encoding='utf-8') as f:
        docs = json.load(f)
        f.close()
    return render_template('index.html', docs=docs)

