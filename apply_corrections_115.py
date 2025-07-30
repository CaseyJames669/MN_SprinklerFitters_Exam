
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 175:
        item['answer'] = "On-tread storage piles, regardless of the storage method, should not exceed 25 ft (7.6 m) in the direction of the wheel holes."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Chapter 18 (Protection of Rubber Tires) and relevant subsections."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
