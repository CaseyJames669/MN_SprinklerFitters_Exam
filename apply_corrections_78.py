
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 123:
        item['answer'] = "NFPA 13 does not specify a universal maximum volume for an antifreeze loop. The focus is on using listed antifreeze solutions at specified maximum concentrations. Some listed products or other standards (like NFPA 13D/13R) might have volume limitations."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 5.3 (General section on antifreeze systems) and specific product listings."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
