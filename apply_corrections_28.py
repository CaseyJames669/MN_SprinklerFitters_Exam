
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 48:
        item['answer'] = "The FDC supply for a dry pipe system should be connected from a tee located between the system control valve and the dry pipe valve. Alternatively, it can be connected to the main piping on the system side of the water supply check valve."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 16.12 (Fire Department Connections) and general principles of dry pipe system design."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
