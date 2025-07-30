
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 110:
        item['answer'] = "100 feet (30.5 meters)."
        item['source'] = "Authority: NFPA, Document: NFPA 14 2022 Edition, Section: Section 7.3.3 (Hose Stations for Class II and Class III Systems)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
