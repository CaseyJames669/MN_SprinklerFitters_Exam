
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 88:
        item['answer'] = "Inspection frequency varies based on cooking volume and type: Monthly for solid fuel cooking operations; Quarterly for high-volume operations; Semi-annually for moderate-volume operations; Annually for low-volume operations."
        item['source'] = "Authority: NFPA, Document: NFPA 96 2024 Edition, Section: Section 12.4 and Table 12.4."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
