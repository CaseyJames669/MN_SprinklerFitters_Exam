
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 42:
        item['answer'] = "For steel pipe, typical maximum hanger spacing is 12 feet for pipe sizes up to 1.25 inches, and 15 feet for pipe sizes 1.5 inches and larger."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 18.4 (General section on hanger spacing for steel pipe)"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
