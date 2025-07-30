
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 41:
        item['answer'] = "Water delivery time to the most remote sprinkler in a dry pipe system is generally limited to 60 seconds for non-residential environments and 15 seconds for dwelling units."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 8.2.4 (Dry Pipe System Water Delivery)"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
