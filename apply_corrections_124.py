
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 183:
        item['answer'] = "The maximum operating pressure for sprinkler systems protecting extra hazard, palletized, solid piled, in bin box, and on shelf storage is determined by the system's design and the pressure rating of its components. While 175 psi is a common working pressure, specific storage protection criteria are detailed in other chapters of NFPA 13."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Chapter 20-25 (Storage Protection) and general principles of system design."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
