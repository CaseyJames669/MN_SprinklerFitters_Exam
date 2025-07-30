
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 53:
        item['answer'] = "A civil penalty not exceeding $1,000 per violation (per day of violation) can be imposed. Additionally, a violation of the State Fire Code can result in a misdemeanor charge."
        item['source'] = "Authority: MN, Document: Statutes, Section: Section 299M.04 (Civil Penalties) and Minnesota State Fire Code (Misdemeanor Charge)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
