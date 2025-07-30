
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 201:
        item['answer'] = "Not Allowed (The use of heat collectors is generally prohibited in NFPA 13)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2016 Edition, Section: General principles of sprinkler installation (prohibition of heat collectors)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
