import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 128:
        item['answer'] = "The \"small room rule\" applies to light hazard occupancies with unobstructed construction and an area of 800 square feet (74 m2) or less. It allows for modifications to sprinkler spacing."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: General principles of sprinkler spacing and design criteria for light hazard occupancies (refer to relevant sections in Chapter 11)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
