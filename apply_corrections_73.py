
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 118:
        item['answer'] = "NFPA 22 does not specify a universal minimum size for a discharge on a tank. The required size is determined by the specific fire protection system being supplied, based on its demand flow rate and required duration."
        item['source'] = "Authority: NFPA, Document: NFPA 22 2023 Edition, Section: Section 5.3 (General section on tank connections and outlets) and general principles of water supply sizing."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
