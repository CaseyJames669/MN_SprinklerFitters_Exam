
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 149:
        item['answer'] = "For wet pipe and preaction systems (not subject to freezing): Less than 5 gallons: Nipple with cap/plug not less than 0.5 inch. Between 5 and 50 gallons: 0.75 inch valve with nipple/cap/plug. 50 gallons or more: Valve not less than 1 inch. For dry pipe and preaction systems (with freezing conditions): Less than 5 gallons: Valve not smaller than 0.5 inch with nipple/cap/plug. More than 5 gallons: Two 1 inch valves separated by a 2 inch x 12 inch condensate nipple or equivalent."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 16.10.5 (Auxiliary Drains)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
