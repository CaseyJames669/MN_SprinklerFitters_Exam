
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 202:
        item['answer'] = "A concentric reducer is typically used to transition from a smaller pump discharge flange to a larger discharge pipe. NFPA 20 requires discharge piping and fittings to be appropriately sized and rated for the maximum total discharge head."
        item['source'] = "Authority: NFPA, Document: NFPA 20 2022 Edition, Section: Section 4.17 (Discharge Pipe and Fittings) and general principles of piping design."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
