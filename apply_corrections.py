import json

input_file_path = "H:\\Google Drive\\MN_SprinklerFitters_Exam\\Grok4 accuracy verification results.json"
output_file_path = "H:\\Google Drive\\MN_SprinklerFitters_Exam\\Grok4 applied corrections.json"

try:
    with open(input_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    corrected_data = []
    for item in data:
        if item.get('correction') and item['correction'] is not None:
            # Apply correction
            item['answer'] = item['correction']['corrected_answer']
            item['source'] = item['correction']['corrected_source']
            # Optionally, remove the 'correction' field after applying
            del item['correction']
            # Set verified to true if a correction was applied
            item['verified'] = True
        corrected_data.append(item)

    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(corrected_data, f, indent=2)

    print(f"Corrections applied and saved to {output_file_path}")

except FileNotFoundError:
    print(f"Error: The file {input_file_path} was not found.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from {input_file_path}. Check file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
