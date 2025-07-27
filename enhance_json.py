

import json
import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
verified_file_path = os.path.join(script_dir, 'Quizlet Full - Verified.json')
enhanced_file_path = os.path.join(script_dir, 'Quizlet Full - Enhanced.json')

def get_tags(question, answer):
    tags = set()
    text_to_search = question.lower() + ' ' + answer.lower()

    # NFPA Standards
    nfpa_matches = re.findall(r'nfpa (\d+[a-z]?)', text_to_search)
    for match in nfpa_matches:
        tags.add(f'NFPA-{match.upper()}')

    # Tagging Keywords
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
    # Key-value pair pattern (e.g., "Key: Value; Key2: Value2")
    kv_matches = re.findall(r'([\w\s]+):\s(.*?)(?:;|$)', answer)
    if len(kv_matches) > 1:
        return {key.strip(): value.strip() for key, value in kv_matches}

    # List pattern (e.g., "A. Item 1 B. Item 2")
    list_matches = re.findall(r'([A-Z])\. (.*?)(?=\s[A-Z]\.|$)', answer)
    if list_matches:
        return [f"{label}. {item.strip()}" for label, item in list_matches]

    # Simple list pattern (e.g., "Item 1, Item 2, Item 3")
    simple_list = [item.strip() for item in answer.split(',')]
    if len(simple_list) > 2:
        return simple_list

    return answer

def standardize_source(source_str):
    # NFPA pattern
    nfpa_match = re.match(r'NFPA (\d+[A-Z]?) (\d{4}) Edition, (Section|Table) (.*)', source_str)
    if nfpa_match:
        doc_num = nfpa_match.group(1)
        edition = nfpa_match.group(2)
        ref_type = nfpa_match.group(3)
        ref = nfpa_match.group(4)
        return f"Authority: NFPA, Document: NFPA {doc_num} {edition} Edition, Section: {ref_type} {ref}"

    # Minnesota State Fire Code pattern
    msfc_match = re.match(r'Minnesota State Fire Code (\d{4}), Section (.*)', source_str)
    if msfc_match:
        edition = msfc_match.group(1)
        ref = msfc_match.group(2)
        return f"Authority: Minnesota, Document: State Fire Code {edition}, Section: {ref}"

    # MN Statutes pattern
    mns_match = re.match(r'MN Statutes Chapter (.*)', source_str)
    if mns_match:
        ref = mns_match.group(1)
        return f"Authority: MN, Document: Statutes, Section: Chapter {ref}"

    # MN Rules pattern
    mnr_match = re.match(r'MN Rules (.*)', source_str)
    if mnr_match:
        ref = mnr_match.group(1)
        return f"Authority: MN, Document: Rules, Section: {ref}"

    # Default case
    return source_str

try:
    with open(verified_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    enhanced_data = []
    for i, item in enumerate(data, 1):
        question = item['question']
        answer = item['answer']

        # Extract source
        source_match = re.search(r'\((.*?)\)', answer)
        if source_match:
            source = source_match.group(1)
            answer_text = answer.replace(f'({source})', '').strip()
        else:
            source = 'N/A'
            answer_text = answer

        # Get tags
        tags = get_tags(question, answer)

        # Format answer
        formatted_answer = format_answer(answer_text)
        
        # Standardize source
        standardized_source = standardize_source(source)

        enhanced_data.append({
            'id': i,
            'question': question,
            'answer': formatted_answer,
            'source': standardized_source,
            'tags': tags
        })

    with open(enhanced_file_path, 'w', encoding='utf-8') as f:
        json.dump(enhanced_data, f, indent=2)

    print(f"Successfully enhanced the file. New JSON written to {enhanced_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

