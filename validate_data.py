import json
import re
from collections import Counter

# Constants
ENHANCED_JSON_PATH = 'Quizlet Full - Enhanced.json'
MIN_WORDS_QUESTION = 3
MIN_WORDS_ANSWER = 1

# Regex for the source format
# Example: "Authority: NFPA, Document: NFPA 25 2023 Edition, Section: Section 7.3.1"
SOURCE_REGEX = re.compile(r'^Authority: [^,]+, Document: [^,]+, Section: .+$')

def load_data(file_path):
    """Loads the JSON data from the specified file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        return None

def validate_data(data):
    """Runs all validation checks and returns a list of errors."""
    errors = []
    
    # Rule 1: ID Validation
    ids = [item.get('id') for item in data if item.get('id') is not None]
    if len(ids) != len(data):
        errors.append("Validation Error: Some items are missing an 'id'.")
    
    # Check for duplicate IDs
    id_counts = Counter(ids)
    duplicate_ids = [item for item, count in id_counts.items() if count > 1]
    if duplicate_ids:
        errors.append(f"Validation Error: Duplicate IDs found: {duplicate_ids}")
        
    # Check for missing IDs in sequence
    if ids:
        expected_ids = set(range(1, max(ids) + 1))
        missing_ids = sorted(list(expected_ids - set(ids)))
        if missing_ids:
            errors.append(f"Validation Error: Missing IDs in sequence: {missing_ids}")

    for i, item in enumerate(data, 1):
        item_id = item.get('id', f"at position {i}")

        # Rule 2: Content Validation
        if not item.get('question', '').strip():
            errors.append(f"Content Error (ID: {item_id}): Question is empty or missing.")
        if not item.get('answer', '').strip():
            errors.append(f"Content Error (ID: {item_id}): Answer is empty or missing.")
        if not item.get('source', '').strip():
            errors.append(f"Content Error (ID: {item_id}): Source is empty or missing.")
        
        tags = item.get('tags', [])
        if not tags or not all(isinstance(t, str) and t.strip() for t in tags):
            errors.append(f"Content Error (ID: {item_id}): Tags list is empty, invalid, or contains empty values.")

        # Rule 3: Source Format Validation
        source = item.get('source', '')
        if source and not SOURCE_REGEX.match(source):
            errors.append(f"Format Error (ID: {item_id}): Source format is incorrect. Got: '{source}'")

        # Rule 4: Length-Based Validation
        question_len = len(item.get('question', '').split())
        answer_len = len(item.get('answer', '').split())
        if question_len < MIN_WORDS_QUESTION:
            errors.append(f"Length Error (ID: {item_id}): Question seems too short ({question_len} words).")
        if answer_len < MIN_WORDS_ANSWER:
            errors.append(f"Length Error (ID: {item_id}): Answer seems too short ({answer_len} words).")
            
    return errors

def main():
    """Main function to load, validate, and report."""
    print(f"Loading data from '{ENHANCED_JSON_PATH}'...")
    data = load_data(ENHANCED_JSON_PATH)
    
    if data is None:
        return

    print("Starting data validation...")
    validation_errors = validate_data(data)
    
    if not validation_errors:
        print("\nValidation Complete: No errors found. The dataset is consistent with the defined rules.")
    else:
        print(f"\nValidation Complete: Found {len(validation_errors)} errors.")
        for error in validation_errors:
            print(f"- {error}")

if __name__ == '__main__':
    main()
