
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 148:
        item['answer'] = "The maximum capacity for a dry pipe system is typically 750 gallons when equipped with quick-opening devices, and 500 gallons without. Specific requirements are detailed in NFPA 13."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 8.2 (Dry Pipe Systems) and relevant subsections on system capacity."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
