
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 208:
        item['answer'] = "False. While jockey pumps themselves are not required to be listed, their controllers are required to be listed (though not specifically for fire pump service)."
        item['source'] = "Authority: NFPA, Document: NFPA 20 2022 Edition, Section: Section 4.27 (Pressure Maintenance (Jockey or Make-Up) Pumps) and relevant subsections on controllers."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
