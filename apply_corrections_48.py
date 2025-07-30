
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 78:
        item['answer'] = "Any pipe material not specifically listed in NFPA 14 for standpipe systems, or not investigated and listed for this service. (Ductile iron pipe is acceptable if listed and meets AWWA C151 or C115 standards)."
        item['source'] = "Authority: NFPA, Document: NFPA 14 2022 Edition, Section: Section 5.1.1 (Acceptable Pipe Materials)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
