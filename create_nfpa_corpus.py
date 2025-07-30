import os
import json
from PyPDF2 import PdfReader
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
NFPA_USER = os.getenv("NFPA_USER")
NFPA_PASS = os.getenv("NFPA_PASS")

# Define relative paths for portability
NFPA_DOCS_DIR = "NFPAs"
CORPUS_FILE = "nfpa_corpus.json"

def create_corpus():
    """
    Extracts text from PDF files in the specified directory and saves it to a JSON corpus file.
    """
    # Example of how you might use the credentials
    if NFPA_USER and NFPA_PASS:
        print(f"Running with user: {NFPA_USER}")
        # Here you would add logic that requires authentication,
        # such as downloading files from a protected server.
    else:
        print("NFPA credentials not found. Running in offline mode.")

    corpus = []
    
    if not os.path.isdir(NFPA_DOCS_DIR):
        print(f"Error: Directory not found at '{NFPA_DOCS_DIR}'")
        return

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

    # Write the corpus to a JSON file
    try:
        with open(CORPUS_FILE, 'w', encoding='utf-8') as f:
            json.dump(corpus, f, indent=2, ensure_ascii=False)
        print(f"NFPA corpus created successfully at '{CORPUS_FILE}'")
    except IOError as e:
        print(f"Error writing to file '{CORPUS_FILE}': {e}")

if __name__ == "__main__":
    create_corpus()
