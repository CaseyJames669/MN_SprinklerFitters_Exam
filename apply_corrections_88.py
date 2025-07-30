
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 137:
        item['answer'] = "Listed antifreeze solutions. Historically, glycerin-based solutions were approved for use with CPVC piping."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 8.6 (Antifreeze Systems) and specific product listings."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
