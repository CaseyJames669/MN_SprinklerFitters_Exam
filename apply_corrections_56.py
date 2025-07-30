
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 89:
        item['answer'] = "Diesel = Weekly for a minimum of 30-minute run time. Electric = Monthly for a minimum of 10-minute run time (weekly under specific conditions). Steam = Refer to manufacturer's instructions and NFPA 25 for specific requirements."
        item['source'] = "Authority: NFPA, Document: NFPA 25 2023 Edition, Section: Section 8.3.3 (Fire Pump Operation)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
