
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 30:
        item['answer'] = "Any pipe material not specifically listed for use in sprinkler systems, or not capable of meeting performance requirements (e.g., withstanding 130 psi at 120°F for non-metallic pipes)."
        item['source'] = "Authority: NFPA, Document: NFPA 13D 2022 Edition, Section: Section 5.2"

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
