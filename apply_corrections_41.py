
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 69:
        item['answer'] = "Preaction system (including vacuum systems, which operate with negative air pressure)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Sections 3.3.222.10 and 3.3.222.11 (Definitions of vacuum dry and preaction systems)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
