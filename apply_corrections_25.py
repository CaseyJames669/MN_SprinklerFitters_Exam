import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 44:
        item['answer'] = [r".75\":8'", r"1.25\"-1.5\":10'", r"2\"-3\":12'", r"3.5\"-8\":15'"]
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 18.4 (General section on hanger spacing for copper tube pipe)"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")