import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
enhanced_file_path = os.path.join(script_dir, 'Quizlet Full - Enhanced.json')
notebooklm_file_path = os.path.join(script_dir, 'Quizlet Full - NotebookLM.txt')

notebooklm_content = ""

try:
    with open(enhanced_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        notebooklm_content += f"**Question:** {item['question']}\n\n"
        notebooklm_content += f"**Answer:** {item['answer']}\n\n"
        notebooklm_content += f"**Source:** {item['source']}\n\n"
        notebooklm_content += f"**Tags:** {', '.join(item['tags'])}\n"
        notebooklm_content += "---\n"

    with open(notebooklm_file_path, 'w', encoding='utf-8') as f:
        f.write(notebooklm_content)

    print(f"Successfully converted to NotebookLM format. New file written to {notebooklm_file_path}")

except Exception as e:
    print(f"An error occurred: {e}")
