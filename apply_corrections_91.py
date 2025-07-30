
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 144:
        item['answer'] = "The predrilled hole size for lag screws is typically 1/16 inch greater than the diameter of the bolt. Specific requirements are detailed in NFPA 13 and manufacturer's instructions."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 18.5.9 (General section on lag screws) and manufacturer's instructions."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
