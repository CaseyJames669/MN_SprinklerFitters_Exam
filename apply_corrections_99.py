
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 154:
        item['answer'] = "The maximum sprinkler spacing for extra hazard systems is determined by the specific design criteria, including the hazard classification, sprinkler type, and hydraulic calculations. Refer to NFPA 13 for detailed tables and requirements."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 11.3 (Extra Hazard Occupancies) and relevant tables."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
