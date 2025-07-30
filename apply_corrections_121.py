
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 181:
        item['answer'] = "10 psi."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Annex A.8.1.2.1 and relevant subsections on air supply and relief valves."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
