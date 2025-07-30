
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 134:
        item['answer'] = "The maximum number of sprinklers allowed on branch lines on either side of a cross main varies based on the occupancy hazard and pipe sizing method. For light hazard occupancies, a common guideline is 8 sprinklers per side."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: General principles of branch line design and pipe schedule tables (refer to Chapter 28 for pipe schedule systems)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
