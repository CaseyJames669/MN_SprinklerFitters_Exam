
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 136:
        item['answer'] = "A standpipe system that contains water at all times and relies exclusively on the fire department connection to supply the system demand."
        item['source'] = "Authority: NFPA, Document: NFPA 14 2022 Edition, Section: Section 3.3.20.5 (Manual Wet Standpipe System)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
