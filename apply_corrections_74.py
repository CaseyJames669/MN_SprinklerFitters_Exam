
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 119:
        item['answer'] = "8 inches (This is a common dimension for lintels, but specific requirements for compartmentation are detailed in NFPA 13)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 9.5.3 (General section on compartmentation) and relevant building codes."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
