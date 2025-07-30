
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 11:
        item['source'] = "Authority: Minnesota, Document: State Fire Code 2020, Section: Section 903.4.4"
    elif item['id'] == 12:
        item['source'] = "Authority: NFPA, Document: NFPA 25 2023 Edition, Section: Sections 9.2.5.1.1 and 9.2.5.1.2"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
