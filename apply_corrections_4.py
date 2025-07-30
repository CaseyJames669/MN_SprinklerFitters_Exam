import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 17:
        item['answer'] = "Check valves with small orifices (like 3/32\") are generally used for pressure equalization or drainage. While specific requirements for such orifices in check valves for freezer spaces are not explicitly detailed in NFPA 13 2025 Section 8.3.2.3, proper design for refrigerated spaces is crucial to prevent ice plugs and ensure system integrity."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 8.8 (Refrigerated Spaces) and general principles of pressure equalization in fire protection systems."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
