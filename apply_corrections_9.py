
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 25:
        item['answer'] = "NFPA 13 does not specify a minimum time for a valve to close. The standard focuses on ensuring valves are open and properly supervised for system readiness."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Not Specified (General principles of valve supervision)"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
