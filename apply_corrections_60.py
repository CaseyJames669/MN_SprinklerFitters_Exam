
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 101:
        item['answer'] = "Yes, horizontal piping from the standpipe to the hose connection should be adequately supported with hangers to prevent sagging and ensure system integrity. Specific spacing requirements are detailed in NFPA 14."
        item['source'] = "Authority: NFPA, Document: NFPA 14 2022 Edition, Section: General principles of pipe support and relevant sections in Chapter 9 (Installation)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
