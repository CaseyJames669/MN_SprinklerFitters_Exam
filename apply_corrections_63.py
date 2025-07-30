
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 104:
        item['answer'] = "The maximum spacing between residential sprinkler heads is determined by the sprinkler's listing and its tested coverage area. Sprinklers must be located no more than half the listed spacing from walls."
        item['source'] = "Authority: NFPA, Document: NFPA 13D 2022 Edition, Section: Section 10.2 (Spacing and Location of Sprinklers)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
