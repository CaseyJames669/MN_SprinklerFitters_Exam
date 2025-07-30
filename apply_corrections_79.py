
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 127:
        item['answer'] = "NFPA 13R requires hydraulic calculations to ensure adequate water supply. The number of sprinklers included in the design area for calculations depends on the specific system design and the hydraulically most remote sprinklers."
        item['source'] = "Authority: NFPA, Document: NFPA 13R 2022 Edition, Section: Section 11.2 (Hydraulic Design) and general principles of hydraulic calculations."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
