
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 206:
        item['answer'] = "Upright sprinklers on pipes 3 inches or larger must be placed on sprigs or offset from the pipe to eliminate obstruction and ensure proper water distribution."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 10.3.5 (Obstructions to Sprinkler Discharge) and general principles of sprinkler installation."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
