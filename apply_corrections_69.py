
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 112:
        item['answer'] = "Sprinklers in attics should be located to provide effective coverage. Common guidelines suggest a maximum distance of 3 ft off center from the peak. Specific requirements for vertical distance from the peak and other spacing criteria are detailed in NFPA 13."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 12.1.1 (General section on attics and concealed spaces) and common design practices."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
