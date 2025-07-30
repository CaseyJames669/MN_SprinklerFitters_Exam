
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 135:
        item['answer'] = "NFPA 13 does not specify a number of sprinkler heads that triggers the requirement for an FDC. FDCs are generally required for automatic fire sprinkler systems with risers greater than 3 inches, or as determined by the authority having jurisdiction."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 16.12 (Fire Department Connections) and general principles of FDC requirements."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
