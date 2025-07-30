
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 165:
        item['answer'] = "NFPA 20 does not specify a minimum mounting height for fire pump controllers. Installation should follow manufacturer's instructions and local codes, ensuring adequate working space and protection."
        item['source'] = "Authority: NFPA, Document: NFPA 20 2022 Edition, Section: General principles of fire pump controller installation."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
