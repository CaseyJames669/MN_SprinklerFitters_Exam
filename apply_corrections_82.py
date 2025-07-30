
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 131:
        item['answer'] = "The minimum square footage for ESFR heads is determined by the sprinkler's listing and the specific design requirements for the occupancy and storage arrangement. The design area for an ESFR system can be increased to 18 sprinklers under certain conditions."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 20.9 (ESFR Sprinkler Design Area) and specific product listings."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
