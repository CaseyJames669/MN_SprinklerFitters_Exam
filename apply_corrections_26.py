
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 45:
        item['answer'] = "Hanger spacing for CPVC pipe is determined by the product's listing and the manufacturer's installation instructions. Refer to manufacturer's data for specific values."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 18.4 (General section on hanger spacing) and CPVC manufacturer's installation instructions."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
