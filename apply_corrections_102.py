
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 161:
        item['answer'] = "The maximum horizontal sprinkler head spacing for in-rack sprinklers varies based on the commodity, storage arrangement, and sprinkler type. Typical spacing is 12 feet, and 8 feet for encapsulated storage. Refer to NFPA 13 for detailed requirements."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Chapter 25 (In-Rack Sprinkler Protection) and relevant tables."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
