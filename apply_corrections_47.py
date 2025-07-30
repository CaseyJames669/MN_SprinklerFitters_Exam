
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 77:
        item['answer'] = "NFPA 13 does not specify a single, universal minimum operating pressure for all sprinkler heads. The required operating pressure is determined through hydraulic calculations based on the specific occupancy hazard, sprinkler type, and design area."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: General principles of hydraulic calculations and sprinkler design."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
