
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 60:
        item['answer'] = "Must not (to prevent solvent cement from entering and potentially clogging the sprinkler head, which could impair its operation)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2016 Edition, Section: Section 8.3.1.4 (Installation of Sprinklers in Fittings)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
