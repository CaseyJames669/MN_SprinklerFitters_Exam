

import json
import re
import os
from collections import Counter

# --- Configuration ---
ORIGINAL_JSON_PATH = 'Quizlet Full - Original.json'
ENHANCED_JSON_PATH = 'Quizlet Full - Enhanced.json'
VALIDATION_REPORT_PATH = 'validation_report.txt'

MIN_WORDS_QUESTION = 3
MIN_WORDS_ANSWER = 1
SOURCE_REGEX = re.compile(r'^Authority: [^,]+, Document: [^,]+, Section: .+$')

# --- Data Processing and Enhancement Functions (from enhance_json.py) ---

def get_tags(question, answer):
    tags = set()
    text_to_search = question.lower() + ' ' + str(answer).lower()
    nfpa_matches = re.findall(r'nfpa (\d+[a-z]?)', text_to_search)
    for match in nfpa_matches:
        tags.add(f'NFPA-{match.upper()}')
    keyword_map = {
        'Piping': ['pipe', 'piping'],
        'Piping-Materials': ['steel', 'copper', 'cpvc', 'ductile iron'],
        'Piping-Support': ['hanger', 'support', 'seismic', 'bracing'],
        'Piping-Dimensions': ['schedule', 'size', 'diameter', 'length', 'pitch'],
        'System-Components': ['valve', 'fitting', 'reducer', 'union', 'gauge', 'fdc'],
        'Sprinklers': ['sprinkler', 'head'],
        'Sprinklers-Spacing': ['spacing', 'coverage', 'distance', 'area'],
        'Sprinklers-Temperature': ['temperature', 'bulb', 'color code'],
        'Sprinklers-Types': ['esfr', 'sidewall', 'upright', 'pendant', 'residential'],
        'Fire-Pumps': ['pump', 'jockey pump', 'controller', 'sensing line'],
        'Water-Supply': ['tank', 'hydrant', 'pressure', 'flow', 'water supply'],
        'System-Types': ['wet', 'dry', 'preaction', 'deluge', 'antifreeze'],
        'Hazard-Classification': ['hazard', 'light', 'ordinary', 'extra'],
        'Installation': ['installation', 'testing', 'acceptance', 'maintenance'],
        'Minnesota-Code': ['minnesota', 'mn']
    }
    for tag, keywords in keyword_map.items():
        for keyword in keywords:
            if keyword in text_to_search:
                tags.add(tag)
    if not tags:
        tags.add('General')
    return sorted(list(tags))

def format_answer(answer):
    if not isinstance(answer, str):
        return answer
    kv_matches = re.findall(r'([\w\s]+):\s(.*?)(?:;|$)', answer)
    if len(kv_matches) > 1:
        return {key.strip(): value.strip() for key, value in kv_matches}
    list_matches = re.findall(r'([A-Z])\. (.*?)(?=\s[A-Z]\.|$)', answer)
    if list_matches:
        return [f"{label}. {item.strip()}" for label, item in list_matches]
    simple_list = [item.strip() for item in answer.split(',')]
    if len(simple_list) > 2:
        return simple_list
    return answer

def standardize_source(source_str):
    if not isinstance(source_str, str):
        return 'Invalid Source Format'

    # NFPA Standard Pattern
    nfpa_match = re.search(r'NFPA (\d+[A-Z]?) (\d{4}) Edition, (Section|Table|Figure|Chapter|A) (.*)', source_str, re.IGNORECASE)
    if nfpa_match:
        doc_num, edition, ref_type, ref = nfpa_match.groups()
        return f"Authority: NFPA, Document: NFPA {doc_num.upper()} {edition} Edition, Section: {ref_type.capitalize()} {ref}"

    # Simplified NFPA Pattern
    nfpa_simple_match = re.search(r'NFPA (\d+[A-Z]?) (\d{4}) Edition', source_str, re.IGNORECASE)
    if nfpa_simple_match:
        doc_num, edition = nfpa_simple_match.groups()
        return f"Authority: NFPA, Document: NFPA {doc_num.upper()} {edition} Edition, Section: Not Specified"

    # Minnesota State Fire Code Pattern
    msfc_match = re.search(r'MN Fire Code (\d{4}), Section (.*)', source_str, re.IGNORECASE)
    if msfc_match:
        edition, ref = msfc_match.groups()
        return f"Authority: Minnesota, Document: State Fire Code {edition}, Section: {ref}"

    # MN Statutes Pattern
    mns_match = re.search(r'MN Statutes Chapter (.*)', source_str, re.IGNORECASE)
    if mns_match:
        ref = mns_match.group(1)
        return f"Authority: MN, Document: Statutes, Section: Chapter {ref}"

    # MN Rules Pattern
    mnr_match = re.search(r'MN Rules (.*)', source_str, re.IGNORECASE)
    if mnr_match:
        ref = mnr_match.group(1)
        return f"Authority: MN, Document: Rules, Section: {ref}"

    # Other known but non-standard formats
    if '10x diameter' in source_str:
        return "Authority: NFPA, Document: NFPA 20 2022 Edition, Section: Section 4.15.3.3"
    if 'Standard hydraulic method' in source_str:
        return "Authority: General, Document: Engineering Principles, Section: Hazen-Williams Formula"
    if 'Various jurisdictions' in source_str:
        return "Authority: Multiple, Document: Building and Fire Codes, Section: Various"

    # Default case for anything that doesn't match
    return f"Authority: Unknown, Document: Unknown, Section: {source_str}"

# --- Validation Functions ---

def validate_data(data):
    errors = []
    ids = [item.get('id') for item in data if item.get('id') is not None]
    if len(ids) != len(data):
        errors.append("Validation Error: Some items are missing an 'id'.")
    id_counts = Counter(ids)
    duplicate_ids = [item for item, count in id_counts.items() if count > 1]
    if duplicate_ids:
        errors.append(f"Validation Error: Duplicate IDs found: {duplicate_ids}")
    if ids:
        expected_ids = set(range(1, max(ids) + 1))
        missing_ids = sorted(list(expected_ids - set(ids)))
        if missing_ids:
            errors.append(f"Validation Error: Missing IDs in sequence: {missing_ids}")
    for i, item in enumerate(data, 1):
        item_id = item.get('id', f"at position {i}")
        if not item.get('question', '').strip():
            errors.append(f"Content Error (ID: {item_id}): Question is empty or missing.")
        if not item.get('answer'):
            errors.append(f"Content Error (ID: {item_id}): Answer is empty or missing.")
        source = item.get('source', '')
        if not source.strip() or not SOURCE_REGEX.match(source):
            errors.append(f"Format Error (ID: {item_id}): Source format is incorrect or missing. Got: '{source}'")
        tags = item.get('tags', [])
        if not tags or not all(isinstance(t, str) and t.strip() for t in tags):
            errors.append(f"Content Error (ID: {item_id}): Tags list is empty, invalid, or contains empty values.")
        question_len = len(item.get('question', '').split())
        answer_len = len(str(item.get('answer', '')).split())
        if question_len < MIN_WORDS_QUESTION:
            errors.append(f"Length Error (ID: {item_id}): Question seems too short ({question_len} words).")
        if answer_len < MIN_WORDS_ANSWER:
            errors.append(f"Length Error (ID: {item_id}): Answer seems too short ({answer_len} words).")
    return errors

# --- Main Execution ---

def main():
    # 1. Read and de-duplicate the original data (from process_json.py)
    try:
        with open(ORIGINAL_JSON_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading original JSON file: {e}")
        return

    unique_questions = {}
    cleaned_data = []
    for item in data:
        question = item.get("question")
        if question and question not in unique_questions:
            unique_questions[question] = True
            cleaned_data.append(item)

    # 2. Enhance the data (from enhance_json.py)
    enhanced_data = []
    for i, item in enumerate(cleaned_data, 1):
        question = item['question']
        answer = item['answer']
        source_match = re.search(r'\((.*?)\)', str(answer))
        if source_match:
            source = source_match.group(1)
            answer_text = str(answer).replace(f'({source})', '').strip()
        else:
            source = 'N/A'
            answer_text = answer

        enhanced_data.append({
            'id': i,
            'question': question,
            'answer': format_answer(answer_text),
            'source': standardize_source(source),
            'tags': get_tags(question, answer_text)
        })

    # 3. Validate the enhanced data
    validation_errors = validate_data(enhanced_data)
    if validation_errors:
        print(f"Found {len(validation_errors)} validation errors. See '{VALIDATION_REPORT_PATH}' for details.")
        with open(VALIDATION_REPORT_PATH, 'w', encoding='utf-8') as f:
            for error in validation_errors:
                f.write(f"- {error}\n")
    else:
        print("Validation successful. No errors found.")

    # 4. Write the final, clean JSON file
    with open(ENHANCED_JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(enhanced_data, f, indent=2)

    print(f"Successfully rebuilt and enhanced the data. New JSON written to {ENHANCED_JSON_PATH}")

if __name__ == '__main__':
    main()

