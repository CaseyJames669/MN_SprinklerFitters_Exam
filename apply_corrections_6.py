
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 20:
        item['answer'] = "Minimum 500 gpm flow at 100 psi residual pressure"
        item['source'] = "Authority: NFPA, Document: NFPA 14 2022 Edition, Section: Section 7.10.1"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
