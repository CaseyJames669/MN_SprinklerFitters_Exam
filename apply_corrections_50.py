
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 81:
        item['answer'] = "18 inches (This is a fundamental clearance requirement for standard spray sprinklers to ensure proper water distribution and prevent obstruction of the spray pattern)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: General principles of sprinkler clearances (refer to relevant sections in Chapter 8 and Chapter 11 for specific clearance requirements)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
