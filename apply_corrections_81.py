import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 130:
        item['answer'] = "There is no single \"universal\" fire protection code. Widely adopted model codes include the International Fire Code (IFC) and the International Building Code (IBC). The Unified Facilities Criteria (UFC) is used by the U.S. Department of Defense."
        item['source'] = "Authority: Multiple, Document: Model Building and Fire Codes (IFC, IBC) and U.S. Department of Defense Criteria (UFC)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
