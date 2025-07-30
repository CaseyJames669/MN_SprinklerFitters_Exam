
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 164:
        item['answer'] = "For pumps with a rated capacity not exceeding 2500 gpm, the automatic relief valve shall have a nominal size of 0.75 inches. For pumps with a rated capacity of 3000 gpm to 5000 gpm, the automatic relief valve shall have a nominal size of 1 inch."
        item['source'] = "Authority: NFPA, Document: NFPA 20 2022 Edition, Section: Section 5.11.1.6"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
