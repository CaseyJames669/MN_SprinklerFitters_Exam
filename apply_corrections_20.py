
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 39:
        item['answer'] = "Yes, pump rooms must be adequately lighted and heated to maintain a minimum temperature of 4°C (40°F) to prevent freezing, and to ensure proper operation and maintenance."
        item['source'] = "Authority: NFPA, Document: NFPA 20 2022 Edition, Section: Section 4.12 (General requirements for fire pump protection, with specific details on lighting and heating found in related sections and building codes)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
