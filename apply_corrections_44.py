
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 73:
        item['answer'] = "The water supply duration for exposure sprinklers varies based on the specific hazard and design requirements. General water supply durations for secondary supplies are typically not less than 30 minutes."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 8.7 (Exposure Protection Sprinkler Systems) and Section 20.15/24.4 (Hose Stream Allowance and Water Supply Duration)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
