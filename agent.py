import json
import hashlib
import os
import argparse
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import google.generativeai as genai
from flask import Flask, render_template_string, request

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

def verify_and_correct_entries(entries, api_key):
    """
    Verifies and corrects entries using the Gemini API.
    """
    if not api_key:
        print("API key not provided. Skipping verification.")
        for entry in entries:
            entry['verified'] = False
            entry['confidence'] = 0.0
            entry['correction'] = ""
        return entries

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

    for i, entry in enumerate(entries):
        print(f"Verifying entry {i+1}/{len(entries)}...")
        question = entry['question']
        answer = entry['answer']

        prompt = f"""
        You are an expert in fire safety standards. Please verify the following question and answer pair against the official NFPA standards (specifically the editions mentioned in the answer).

        Question: '{question}'
        Answer: '{answer}'

        Please respond with a JSON object with the following structure:
        {{
          "is_correct": boolean,
          "corrected_answer": "The corrected answer if is_correct is false, otherwise the original answer.",
          "confidence_score": float (from 0.0 to 1.0),
          "explanation": "A brief explanation of why the answer is correct or incorrect, citing the relevant standard and section."
        }}

        Only provide the JSON object in your response.
        """

        try:
            response = model.generate_content(prompt)
            response_text = response.text
            response_json = json.loads(response_text)

            entry['verified'] = response_json.get('is_correct', False)
            entry['confidence'] = response_json.get('confidence_score', 0.0)
            if not response_json.get('is_correct'):
                entry['answer'] = response_json.get('corrected_answer', answer)
                entry['correction'] = response_json.get('explanation', '')

        except Exception as e:
            print(f"An error occurred while verifying entry {i+1}: {e}")
            entry['verified'] = False
            entry['confidence'] = 0.0
            entry['correction'] = f"Error during verification: {e}"

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

def generate_new_entries(entries, api_key, num_to_generate=10):
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
        if not entry.get('verified', False) and entry.get('correction'):
             story.append(Paragraph(f"<font color='red'><b>Correction:</b> {entry['correction']}</font>", styles['Normal']))
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

def list_gemini_models(api_key):
    genai.configure(api_key=api_key)
    print("Available Gemini Models:")
    for m in genai.list_models():
        if "generateContent" in m.supported_generation_methods:
            print(f"  {m.name}")

def main():
    parser = argparse.ArgumentParser(description='AI agent for processing sprinkler fitter exam data.')
    parser.add_argument('--input', type=str, default='Quizlet Full - Original.json', help='Input JSON file.')
    parser.add_argument('--output', type=str, default='Quizlet Full - Enhanced.json', help='Output JSON file.')
    parser.add_argument('--generate_new', type=int, default=10, help='Number of new Q&A pairs to generate.')
    parser.add_argument('--skip_verification', action='store_true', help='Skip the verification step.')
    parser.add_argument('--run_web_app', action='store_true', help='Run the web app.')
    parser.add_argument('--api_key', type=str, default=None, help='Gemini API key.')
    args = parser.parse_args()

    # Load the input data
    with open(args.input, 'r', encoding='utf-8') as f:
        entries = json.load(f)

    # Process the entries
    entries = deduplicate_entries(entries)
    entries = verify_and_correct_entries(entries, args.api_key)
    entries = enhance_entries(entries)
    
    if args.generate_new > 0:
        new_entries = generate_new_entries(entries, args.api_key, args.generate_new)
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