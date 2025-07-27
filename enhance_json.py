

import json
import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
verified_file_path = os.path.join(script_dir, 'Quizlet Full - Verified.json')
enhanced_file_path = os.path.join(script_dir, 'Quizlet Full - Enhanced.json')

def get_tags(question, answer):
    tags = set()
    # Add NFPA tags
    nfpa_matches = re.findall(r'NFPA (\d+[A-Z]?)', question + ' ' + answer)
    for match in nfpa_matches:
        tags.add(f'NFPA {match}')

    # Add other relevant tags
    if 'hanger' in question.lower():
        tags.add('Hangers')
    if 'pipe' in question.lower():
        tags.add('Piping')
    if 'pump' in question.lower():
        tags.add('Fire Pumps')
    if 'standpipe' in question.lower():
        tags.add('Standpipes')
    if 'hazard' in question.lower():
        tags.add('Hazard Classification')
    if 'spacing' in question.lower() or 'coverage' in question.lower():
        tags.add('Sprinkler Spacing')

    return list(tags) if tags else ['General']

def format_answer(answer):
    # Split lists into Markdown format
    if ' = ' in answer and ' run time' in answer:
        parts = answer.split(' (NFPA')[0].split(' ')
        formatted_parts = []
        for i in range(0, len(parts), 4):
            formatted_parts.append(f'- {parts[i]} {parts[i+1]} {parts[i+2]} {parts[i+3]}')
        return '\n'.join(formatted_parts) + f'\n(NFPA{answer.split("(NFPA")[1]}'
    return answer

try:
    with open(verified_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    enhanced_data = []
    for item in data:
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

        enhanced_data.append({
            'question': question,
            'answer': formatted_answer,
            'source': source,
            'tags': tags
        })

    with open(enhanced_file_path, 'w', encoding='utf-8') as f:
        json.dump(enhanced_data, f, indent=2)

    print(f"Successfully enhanced the file. New JSON written to {enhanced_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")

