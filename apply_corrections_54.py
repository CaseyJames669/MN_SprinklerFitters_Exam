
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 86:
        item['answer'] = "Weekly for all valves; Monthly for valves secured with locks or supervised; Quarterly for electrically supervised valves."
        item['source'] = "Authority: NFPA, Document: NFPA 25 2023 Edition, Section: Section 13.3.2 (Inspection of Control Valves)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
