
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 132:
        item['answer'] = "A documentation cabinet containing, at a minimum, final record of completion documents, final shop drawings, and as-builts of the fire sprinkler system. Copies of all required signage shall also be kept in this cabinet."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 16.11.1.3 (Documentation Cabinet)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
