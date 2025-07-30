
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 168:
        item['answer'] = "For 10-inch pipe, the required hanger rod size is 5/8 inch. For 12-inch pipe, the required hanger rod size is 3/4 inch."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Table 17.2.1.1 (Hanger Rod Sizes) and relevant tables."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
