
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 138:
        item['answer'] = "32 inches to 40 inches (800 mm to 1000 mm) above the final grade."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2022 Edition, Section: Section 16.9.8 (Post-Indicator Valves)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
