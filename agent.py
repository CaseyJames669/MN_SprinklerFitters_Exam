

import json
import hashlib
import os
import argparse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def deduplicate_entries(entries):
    """
    Deduplicates a list of entries based on a hash of the question and answer.
    """
    unique_entries = []
    seen_hashes = set()
    for entry in entries:
        entry_hash = hashlib.md5(json.dumps(entry, sort_keys=True).encode('utf-8')).hexdigest()
        if entry_hash not in seen_hashes:
            unique_entries.append(entry)
            seen_hashes.add(entry_hash)
    return unique_entries

def verify_and_correct_entries(entries, nfpa_corpus):
    """
    Verifies and corrects entries against the NFPA corpus.
    This is a placeholder for the actual verification logic.
    In a real implementation, this would involve NLP and searching the corpus.
    """
    # For now, we'll just return the entries as is.
    # In a real implementation, you would use an LLM to verify and correct the entries.
    # Example:
    # for entry in entries:
    #     question = entry['question']
    #     answer = entry['answer']
    #     # Use an LLM to check if the answer is correct based on the nfpa_corpus
    #     # If the answer is incorrect, update it.
    #     # You can also add a "verified" flag to the entry.
    #     entry['verified'] = True
    return entries

def enhance_entries(entries):
    """
    Enhances entries by adding a unique ID and tags.
    """
    for i, entry in enumerate(entries):
        entry['id'] = i
        entry['tags'] = extract_tags(entry['question'], entry['answer'])
    return entries

def extract_tags(question, answer):
    """
    Extracts tags from the question and answer.
    This is a placeholder for the actual tag extraction logic.
    """
    tags = []
    if 'NFPA 13' in answer:
        tags.append('NFPA 13')
    if 'NFPA 14' in answer:
        tags.append('NFPA 14')
    if 'NFPA 20' in answer:
        tags.append('NFPA 20')
    if 'NFPA 25' in answer:
        tags.append('NFPA 25')
    if 'Minnesota' in answer:
        tags.append('Minnesota')
    if not tags:
        tags.append('General')
    return tags

def generate_new_entries(entries, nfpa_corpus, num_to_generate=10):
    """
    Generates new question and answer pairs based on the NFPA corpus.
    This is a placeholder for the actual generation logic.
    """
    # For now, we'll just return an empty list.
    # In a real implementation, you would use an LLM to generate new entries.
    return []

def generate_quizlet_file(entries, output_path):
    """
    Generates a text file for Quizlet import.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        for entry in entries:
            f.write(f"{entry['question']}\t{entry['answer']}\n")

def generate_notebooklm_file(entries, output_path):
    """
    Generates a text file for NotebookLM.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        for entry in entries:
            f.write(f"Question: {entry['question']}\n")
            f.write(f"Answer: {entry['answer']}\n\n")

def generate_pdf_study_guide(entries, output_path):
    """
    Generates a PDF study guide.
    """
    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    for entry in entries:
        story.append(Paragraph(f"<b>Question:</b> {entry['question']}", styles['Normal']))
        story.append(Paragraph(f"<b>Answer:</b> {entry['answer']}", styles['Normal']))
        story.append(Paragraph(f"<i>Tags: {', '.join(entry['tags'])}</i>", styles['Normal']))
        story.append(Spacer(1, 12))
    doc.build(story)

from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/')
def quiz():
    return render_template_string('''
    <!doctype html>
    <html>
    <head><title>Sprinkler Fitter Exam Quiz</title></head>
    <body>
        <h1>Sprinkler Fitter Exam Quiz</h1>
        <form method="post" action="/score">
            {% for entry in entries %}
                <div>
                    <p><b>Question:</b> {{ entry.question }}</p>
                    <input type="text" name="answer_{{ entry.id }}" size="100">
                </div>
            {% endfor %}
            <br>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    ''', entries=app.config['entries'])

@app.route('/score', methods=['POST'])
def score():
    score = 0
    for entry in app.config['entries']:
        user_answer = request.form.get(f'answer_{{entry.id}}')
        if user_answer and user_answer.lower() in entry['answer'].lower():
            score += 1
    return f'<h1>Your score: {score}/{len(app.config["entries"])}</h1>'

def run_web_app(entries):
    app.config['entries'] = entries
    app.run(debug=True)

def main():
    parser = argparse.ArgumentParser(description='AI agent for processing sprinkler fitter exam data.')
    parser.add_argument('--input', type=str, default='Quizlet Full - Original.json', help='Input JSON file.')
    parser.add_argument('--output', type=str, default='Quizlet Full - Enhanced.json', help='Output JSON file.')
    parser.add_argument('--generate_new', type=int, default=10, help='Number of new Q&A pairs to generate.')
    parser.add_argument('--skip_verification', action='store_true', help='Skip the verification step.')
    parser.add_argument('--run_web_app', action='store_true', help='Run the web app.')
    args = parser.parse_args()

    # Load the input data
    with open(args.input, 'r', encoding='utf-8') as f:
        entries = json.load(f)

    # Load the NFPA corpus
    nfpa_corpus = {}
    if not args.skip_verification:
        if os.path.exists('nfpa_corpus.json'):
            with open('nfpa_corpus.json', 'r', encoding='utf-8') as f:
                nfpa_corpus = json.load(f)

    # Process the entries
    entries = deduplicate_entries(entries)
    if not args.skip_verification:
        entries = verify_and_correct_entries(entries, nfpa_corpus)
    entries = enhance_entries(entries)
    new_entries = generate_new_entries(entries, nfpa_corpus, args.generate_new)
    entries.extend(new_entries)

    # Save the enhanced data
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2)

    # Generate the output files
    generate_quizlet_file(entries, 'Quizlet Full - FormattedForImport.txt')
    generate_notebooklm_file(entries, 'Quizlet Full - NotebookLM.txt')
    generate_pdf_study_guide(entries, 'study_guide.pdf')

    print(f"Processed {len(entries)} entries. Outputs generated. Repo takeover complete!")

    if args.run_web_app:
        run_web_app(entries)

if __name__ == '__main__':
    main()
