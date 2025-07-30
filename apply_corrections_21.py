
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 40:
        item['answer'] = "In pipe schedule systems, the maximum number of sprinklers allowed on a given pipe size varies based on the occupancy hazard and the specific pipe schedule tables provided in NFPA 13. For branch lines, it is generally limited to eight sprinklers on either side of a cross main, with exceptions for specific conditions."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Chapter 28 (Pipe Schedule Systems) and relevant tables within that chapter."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
