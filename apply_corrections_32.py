
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 54:
        item['answer'] = "The maximum floor area protected by a single sprinkler system (system area limitation) for light hazard wet pipe systems that are electrically supervised is 78,000 square feet (in the 2025 edition). NFPA 13 Section 5.2 defines light hazard occupancies based on content and combustibility."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 4.4.1 (System Area Limitations) and Section 5.2 (Light Hazard Occupancies)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
