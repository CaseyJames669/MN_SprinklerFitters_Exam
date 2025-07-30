
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 145:
        item['answer'] = "1.5 inches (This is a common maximum pipe size for toggle hangers, but specific limitations depend on the hanger's listing and the pipe's weight. Refer to NFPA 13 for detailed tables)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 18.5.7 (General section on toggle hangers) and relevant tables."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
