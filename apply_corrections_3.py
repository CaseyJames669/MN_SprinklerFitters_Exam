import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 15:
        item['answer'] = "For steel pipe, the maximum unsupported length from the end sprinkler to the last hanger on a branch line is typically 36 inches (1\") to 60 inches (1.5\"+). Refer to NFPA 13 for specific tables based on pipe size and material."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 18.5.5"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
