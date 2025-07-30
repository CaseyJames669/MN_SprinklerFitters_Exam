
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 29:
        item['answer'] = "NFPA 231C governed rack storage. This standard was withdrawn in 1999, and its content was incorporated into NFPA 13 (specifically Chapter 25 in the 2025 edition) and NFPA 230."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Chapter 25 (formerly NFPA 231C)"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
