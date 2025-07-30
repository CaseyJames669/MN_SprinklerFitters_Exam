
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 55:
        item['answer'] = "The maximum floor area protected by a single sprinkler system (system area limitation) for ordinary hazard wet pipe systems is typically 52,000 square feet. The maximum coverage area for a single sprinkler in ordinary hazard occupancies is generally 130 square feet. NFPA 13 Section 5.3 defines ordinary hazard occupancies based on content and combustibility."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 4.4.1 (System Area Limitations) and Section 5.3 (Ordinary Hazard Occupancies)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
