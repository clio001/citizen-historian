from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

