
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 120:
        item['answer'] = "When dealing with vertical ceiling height changes, sprinkler spacing must be adjusted to ensure proper coverage. Specific requirements are detailed in NFPA 13, particularly for sloped ceilings and high ceilings."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 11.1 (General section on sprinkler spacing and location) and relevant sections on sloped and high ceilings."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
