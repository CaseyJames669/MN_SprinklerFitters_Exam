
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 99:
        item['answer'] = "At least two-thirds (⅔) full of water."
        item['source'] = "Authority: NFPA, Document: NFPA 25 2023 Edition, Section: Section 9.3 (General section on pressure tank testing and maintenance)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
