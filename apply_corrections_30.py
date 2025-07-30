
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 52:
        item['answer'] = "The Minnesota State Fire Code is primarily based on the International Fire Code (IFC) with state-specific amendments. Minnesota Statute Chapter 299M pertains to Fire Protection Industry Licensing."
        item['source'] = "Authority: MN, Document: State Fire Code (based on IFC) and Statutes, Section: Chapter 299M (Fire Protection Industry Licensing)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
