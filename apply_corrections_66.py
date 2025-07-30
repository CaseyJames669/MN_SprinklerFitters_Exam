
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 108:
        item['answer'] = "Sprinklers are generally not required in: Porches, balconies, lanais, verandas, awnings, carports, porte cocheres, stairs, corridors not part of a means of egress, or similar open and attached features (Section 6.6.5). Also, certain closets and concealed spaces not used for living or storage may be omitted."
        item['source'] = "Authority: NFPA, Document: NFPA 13R 2022 Edition, Section: Section 6.6 (Areas Not Required to Be Sprinklered)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
