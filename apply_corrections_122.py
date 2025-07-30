
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 182:
        item['answer'] = "All system components, both aboveground and underground, must be rated for the system's working pressure and capable of withstanding specified test pressures. Historically, sprinkler systems were rated for not less than 175 psi cold water pressure."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 29.2.1 (Hydrostatic Testing) and general principles of component rating."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
