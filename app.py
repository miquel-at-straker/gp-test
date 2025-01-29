from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)

# Function to load properties (now JSON) based on language
def get_properties(lang):
    en_filepath = os.path.join(os.getcwd(), 'resources', 'en.json')
    es_filepath = os.path.join(os.getcwd(), 'resources', 'es.json')
    ja_filepath = os.path.join(os.getcwd(), 'resources', 'ja.json')

    with open(en_filepath, 'r', encoding='utf-8') as en_file:
        en_properties = json.load(en_file)

    if lang == 'es':
        with open(es_filepath, 'r', encoding='utf-8') as es_file:
            es_properties = json.load(es_file)
        # Merge dictionaries, giving priority to Spanish keys
        properties = {**en_properties, **es_properties}
    elif lang == 'ja':
        with open(ja_filepath, 'r', encoding='utf-8') as ja_file:
            ja_properties = json.load(ja_file)
        # Merge dictionaries, giving priority to Japanese keys
        properties = {**en_properties, **ja_properties}
    else:
        properties = en_properties

    return properties

@app.route('/')
def index():
    lang = request.accept_languages.best_match(['es', 'ja', 'en'])
    properties = get_properties(lang)
    return render_template('index.html', strings=properties)

if __name__ == '__main__':
    app.run(debug=True)