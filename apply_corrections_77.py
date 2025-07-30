
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 122:
        item['answer'] = "For new installations, an air pressure leakage test at 40 psi for 24 hours allows a maximum loss of 1.5 psi. For periodic testing, a 40 psi test for 2 hours allows a maximum loss of 3 psi. (NFPA 25 does not specify a weekly air leakage allowance)."
        item['source'] = "Authority: NFPA, Document: NFPA 25 2023 Edition, Section: Section 13.5.1 (Air Pressure Leakage Tests)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
