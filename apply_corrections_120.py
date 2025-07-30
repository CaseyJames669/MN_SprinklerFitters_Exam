
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 180:
        item['answer'] = "15 psi (based on the given 5:1 ratio and 75 psi system pressure. The actual trip pressure ratio is a characteristic of the specific dry pipe valve model)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 8.2 (Dry Pipe Systems) and manufacturer's data for dry pipe valves."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
