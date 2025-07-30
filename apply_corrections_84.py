
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 133:
        item['answer'] = "While NFPA 20 does not specify a universal 1-inch clearance for pipes passing through walls in a pump house, adequate clearance is required to ensure proper installation, maintenance, and to prevent damage. General guidelines suggest maintaining sufficient space around piping and equipment."
        item['source'] = "Authority: NFPA, Document: NFPA 20 2022 Edition, Section: Section 4.13 (Pipe and Fittings) and general principles of pump house design and clearances."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
