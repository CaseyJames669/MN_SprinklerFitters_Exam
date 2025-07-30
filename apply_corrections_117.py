import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 155:
        item['answer'] = "For unobstructed construction, the sprinkler deflector is typically required to be located between 1 inch and 12 inches from the ceiling."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 11.2.4.1.1.1"
    elif item['id'] == 156:
        item['answer'] = "Not more than 6 inches (150 mm) nor less than 4 inches (100 mm) from ceilings."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 11.3.5.1.1.1"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")