import os
import json
from PyPDF2 import PdfReader

NFPA_DOCS_DIR = "C:\\Users\\casey\\Github\\MN_SprinklerFitters_Exam\\NFPAs"
CORPUS_FILE = "C:\\Users\\casey\\Github\\MN_SprinklerFitters_Exam\\nfpa_corpus.json"

def create_corpus():
    corpus = []
    for filename in os.listdir(NFPA_DOCS_DIR):
        if filename.endswith(".pdf"):
            filepath = os.path.join(NFPA_DOCS_DIR, filename)
            text_content = ""
            try:
                with open(filepath, 'rb') as f:
                    reader = PdfReader(f)
                    for page in reader.pages:
                        text_content += page.extract_text() or ""
                corpus.append({"filename": filename, "content": text_content})
                print(f"Extracted text from {filename}")
            except Exception as e:
                print(f"Error extracting text from {filename}: {e}")

    with open(CORPUS_FILE, 'w', encoding='utf-8') as f:
        json.dump(corpus, f, indent=2)
    print(f"NFPA corpus created at {CORPUS_FILE}")

if __name__ == "__main__":
    create_corpus()
