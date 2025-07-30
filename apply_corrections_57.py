
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 94:
        item['answer'] = "For residential sprinkler systems designed under NFPA 13, calculations typically involve a design area of four (4) most hydraulically remote sprinklers operating simultaneously."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 27.2.4 (General section on hydraulic calculations for residential occupancies) and common design practices."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
