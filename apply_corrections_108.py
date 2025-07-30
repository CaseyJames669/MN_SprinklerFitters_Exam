
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 169:
        item['answer'] = "Horizontal piping from a standpipe to a hose valve should be adequately supported with hangers. Specific spacing requirements, including maximum unsupported lengths, are detailed in NFPA 14 and NFPA 13."
        item['source'] = "Authority: NFPA, Document: NFPA 14 2022 Edition, Section: General principles of pipe support (refer to Section 9.11 for pipe support and NFPA 13 for detailed hanger spacing)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
