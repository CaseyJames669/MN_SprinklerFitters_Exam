
from flask import Flask, render_template, jsonify
import json
import os
import re
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Correctly determine the path to the JSON files
script_dir = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_dir, '..', 'Quizlet Full - Enhanced.json')
corpus_file_path = os.path.join(script_dir, '..', 'nfpa_corpus.json')

# Load data and corpus once at startup
app_data = []
nfpa_corpus = []

def load_data():
    global app_data
    with open(json_file_path, 'r', encoding='utf-8') as f:
        app_data = json.load(f)

def load_corpus():
    global nfpa_corpus
    with open(corpus_file_path, 'r', encoding='utf-8') as f:
        nfpa_corpus = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    return jsonify(app_data)

@app.route('/api/search_nfpa')
def search_nfpa():
    query = request.args.get('query', '')
    results = []
    if query:
        for doc in nfpa_corpus:
            content = doc['content']
            filename = doc['filename']
            # Simple case-insensitive search
            for line in content.splitlines():
                if re.search(r'\b' + re.escape(query) + r'\b', line, re.IGNORECASE):
                    results.append({
                        'filename': filename,
                        'snippet': line.strip()
                    })
    return jsonify(results)

if __name__ == '__main__':
    load_data()
    load_corpus()
    app.run(debug=True)
