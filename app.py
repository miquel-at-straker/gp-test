from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

# Function to load properties (now JSON) based on language
def get_properties(lang):
    if lang == 'es':
        filepath = os.path.join(os.getcwd(), 'resources', 'es.json')
    else:
        filepath = os.path.join(os.getcwd(), 'resources', 'en.json')
    
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route('/')
def index():
    lang = request.accept_languages.best_match(['es', 'en'])
    properties = get_properties(lang)
    return render_template('index.html', strings=properties)

if __name__ == '__main__':
    app.run(debug=True)