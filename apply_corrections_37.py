
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 62:
        item['answer'] = "The specific pipe diameter for air supply lines entering freezer areas is not publicly detailed in NFPA 13 2025 summaries. However, such lines are required to be at least 6 feet long. Refer to the full NFPA 13 standard for precise requirements."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 8.2.3 (Dry Pipe Systems in Refrigerated Spaces)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
