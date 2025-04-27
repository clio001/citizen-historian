from flask_frozen import Freezer

# instead of "filename," below, use the name of the file that
# runs YOUR Flask app - omit .py from the filename
from app import app

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

@freezer.register_generator
def item_nr():
    with open('static/db/docs.json', 'r', encoding="utf-8", errors="ignore") as f:
        docs = json.load(f)
    
    for item in docs:
        yield 'item_nr', {'item_id': item["id"]}
        
@freezer.register_generator
def empire_nr():
    with open('static/db/exploring.json', 'r', encoding="utf-8", errors="ignore") as f:
        docs = json.load(f)
        
    for item in docs:
        yield 'empire_nr', {'item_id': item["id"]}


if __name__ == '__main__':
    freezer.freeze()