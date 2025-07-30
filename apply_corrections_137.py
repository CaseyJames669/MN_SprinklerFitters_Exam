
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 200:
        item['answer'] = "For horizontal split-case fire pumps, elbows and tees with a centerline plane perpendicular to the horizontal split-case pump shaft are permitted at any location in the pump suction intake (no minimum distance requirement)."
        item['source'] = "Authority: NFPA, Document: NFPA 20 2022 Edition, Section: Section 4.15.3.3 (Suction Piping)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
