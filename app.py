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


@app.route('/item/')
def item():
    with open('static/db/docs.json', 'r', encoding='utf-8') as f:
        docs = json.load(f)
        f.close()
    return render_template('item.html', doc=docs[6])

@app.route('/item/<int:item_id>/')
def item_nr(item_id):
    with open('static/db/docs.json', 'r', encoding="utf-8", errors="ignore") as f:
        docs = json.load(f)
    
    for item in docs:
        if item["id"] == item_id:
            selectedItem = item
    
    return render_template("item.html", doc=selectedItem)
    

@app.route('/british-empire-for-children/')
def empire():
    with open('static/db/exploring.json', 'r', encoding="utf-8", errors="ignore") as f:
        docs = json.load(f)
    
    return render_template("empire.html", docs=docs)

@app.route('/british-empire-for-children/item/<int:item_id>/')
def empire_nr(item_id):
    with open('static/db/exploring.json', 'r', encoding="utf-8") as f:
        docs = json.load(f)
    
    for item in docs:
        if item["id"] == item_id:
            selectedItem = item
            
    
    return render_template("empire_item.html", doc=selectedItem)