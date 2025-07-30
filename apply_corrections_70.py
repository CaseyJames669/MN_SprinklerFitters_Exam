
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 113:
        item['answer'] = "Sprinklers are generally not required in clothes closets, linen closets, or pantries within housing units, guest rooms, or guest suites of hotels or motels, provided the total space does not exceed 24 square feet and the walls and ceiling are surfaced with noncombustible or limited-combustible materials."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 9.5.5.13 (Omission of Sprinklers in Closets) and NFPA 13R 2022 Edition, Section: Section 6.6.3."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
