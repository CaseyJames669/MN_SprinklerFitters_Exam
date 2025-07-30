
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 57:
        item['answer'] = "The maximum square footage for storage zones is not directly specified in NFPA 13 Section 5.5. Storage protection requirements, including design areas and densities, are detailed in other chapters of NFPA 13 (e.g., Chapters 20-25), and vary based on commodity classification, storage arrangement, and sprinkler type."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Chapters 20-25 (Storage Protection) and Section 5.5 (General section on water supplies, not storage zones)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
