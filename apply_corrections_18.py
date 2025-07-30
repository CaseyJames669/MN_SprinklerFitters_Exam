
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 35:
        item['answer'] = "Discharge nozzles must be listed for their intended use, and the specific orifice size is determined by the manufacturer's design, installation, and maintenance manual for the listed system."
        item['source'] = "Authority: NFPA, Document: NFPA 17A 2024 Edition, Section: Section 4.3 (Discharge Nozzles)"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
