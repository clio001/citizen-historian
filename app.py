from flask import Flask, render_template, request, redirect, url_for
import json


app = Flask(__name__)

@app.route('/')
def index():
    with open('static/db/docs.json', 'r', encoding='utf-8') as f:
        docs = json.load(f)
        f.close()
    
    with open('static/db/articles.json', 'r', encoding='utf-8') as f:
        articles = json.load(f)
        f.close()

    with open('static/db/blogs.json', 'r', encoding='utf-8') as f:
        blogs = json.load(f)
        f.close()

    with open('static/db/backyard.json', 'r', encoding='utf-8') as f:
        backyard = json.load(f)
        f.close()
        
    return render_template('index.html', docs=docs, articles=articles, blogs=blogs, backyard=backyard)


@app.route('/item')
def item():
    return render_template('item.html')