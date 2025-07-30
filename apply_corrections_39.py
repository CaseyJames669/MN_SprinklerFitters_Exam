
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 65:
        item['answer'] = "Up to 12 inches (This is a common guideline to ensure proper sprinkler operation and avoid obstructions, though specific details for this exact distance in NFPA 13 2025 Section 11.2.5.2.3 are not publicly available)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 11.2.5 (General section on suspended ceilings and obstructions) and general principles of sprinkler installation."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
