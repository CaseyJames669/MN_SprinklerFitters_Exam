
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 184:
        item['answer'] = "The minimum operating pressure of an in-rack sprinkler head varies based on the sprinkler type, commodity classification, and specific design requirements. A common minimum discharge pressure for some in-rack sprinkler types is 15 psi."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Chapter 25 (In-Rack Sprinkler Protection) and relevant tables."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
