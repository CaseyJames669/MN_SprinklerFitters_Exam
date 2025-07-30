import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 5:
        item['answer'] = "For Extra Hazard occupancies with ceiling heights greater than 30 feet, a minimum design density of 0.45 gpm/sq ft is required."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 19.2.3.5.2"
    elif item['id'] == 7:
        item['answer'] = "Coverage area for storage heads varies significantly based on commodity classification, storage height, and sprinkler type. Refer to NFPA 13, Chapters 20-25 for specific requirements."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Chapters 20-25"
    elif item['id'] == 8:
        item['answer'] = "Calculated based on system demand; often a factory pre-charge of 30 psi for hydropneumatic tanks."
        item['source'] = "Authority: NFPA, Document: NFPA 22 2023 Edition, Section: Section 4.1.1"
    elif item['id'] == 9:
        item['answer'] = "Branch lines for Class II systems cannot be smaller than 2.5 inches (65 mm). Main standpipe risers for Class I and Class III systems have a minimum size of 4 inches (100 mm)."
        item['source'] = "Authority: NFPA, Document: NFPA 14 2022 Edition, Section: Section 7.2.1"

# Re-assign IDs sequentially
for i, item in enumerate(data):
    item['id'] = i + 1

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied and IDs re-sequenced.")
