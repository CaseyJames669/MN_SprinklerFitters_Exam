
import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Quizlet Full - Original.json')
output_file_path = os.path.join(script_dir, 'Quizlet Full - Verified.json')

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if data and isinstance(data[-1], dict) and "Sidewall sprinkler head First, the user says" in data[-1].get("question", ""):
        data.pop()

    unique_questions = {}
    cleaned_data = []
    for item in data:
        question = item.get("question")
        if question and question not in unique_questions:
            unique_questions[question] = True
            cleaned_data.append(item)

    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, indent=2)

    print(f"Successfully processed the file. Verified and cleaned JSON written to {output_file_path}")

except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
