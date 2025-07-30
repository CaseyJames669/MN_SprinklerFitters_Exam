
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 178:
        item['answer'] = "For pressure tanks, the distance between the floor and any part of the tank shall be at least 3 feet (0.91 m)."
        item['source'] = "Authority: NFPA, Document: NFPA 22 2023 Edition, Section: Chapter 7 (Pressure Tanks) and relevant subsections."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
