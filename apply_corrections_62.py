
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 103:
        item['answer'] = "NFPA 13D does not specify a universal minimum discharge for a single residential sprinkler head. The required discharge is determined through hydraulic calculations based on the specific design area (typically one or two hydraulically most demanding sprinklers) and the sprinkler's K-factor and pressure."
        item['source'] = "Authority: NFPA, Document: NFPA 13D 2022 Edition, Section: Section 11.1 (Hydraulic Design) and general principles of hydraulic calculations."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
