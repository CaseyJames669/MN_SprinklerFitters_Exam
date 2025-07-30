
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 152:
        item['answer'] = "The maximum distance between branch lines in ordinary hazard occupancies is determined by the sprinkler's listed coverage area and the specific design criteria. For standard spray sprinklers, the maximum spacing between sprinklers on a branch line is typically 15 feet, and the maximum distance between branch lines is also typically 15 feet."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 11.2 (Spacing and Location of Sprinklers) and relevant tables for ordinary hazard occupancies."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
