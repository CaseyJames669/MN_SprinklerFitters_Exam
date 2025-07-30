
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 205:
        item['answer'] = "No (Installing a paddle-type water flow switch on the bottom of a horizontal main is generally not acceptable due to potential for sediment accumulation and false alarms)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 17.17 (Waterflow Alarms) and general principles of flow switch installation."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
