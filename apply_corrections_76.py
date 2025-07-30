
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 121:
        item['answer'] = "Upright sprinklers, sidewall sprinklers (where water cannot be trapped), listed dry pendent or dry sidewall sprinklers, and pendent or sidewall sprinklers off return bends."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 8.2 (Dry Pipe Systems) and Section 8.4 (Types of Sprinklers)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
