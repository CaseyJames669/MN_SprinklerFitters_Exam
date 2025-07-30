
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 176:
        item['answer'] = "For standard spray sprinklers, a minimum of 18 inches (457 mm) shall be maintained. For large drop sprinklers (e.g., ESFR), the minimum clearance is 36 inches (914 mm)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: General principles of sprinkler clearances (refer to relevant sections in Chapter 8 and Chapter 11 for specific clearance requirements)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
