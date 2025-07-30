
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 72:
        item['answer'] = "False. Powder-driven studs are generally not permitted for hangers in new installations in certain seismic categories, but can be used for restraints. Welded studs are used in specific seismic bracing applications. The requirement for couplings depends on the specific application and listed components, not a universal rule for all studs."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 18.5.3 (General section on fasteners and supports) and general principles of listed components and seismic bracing."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
