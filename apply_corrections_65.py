
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 106:
        item['answer'] = "Blue (indicating a High temperature rating, typically 250-300°F, suitable for areas with elevated ambient temperatures due to heat sources)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Table 7.2.4.1 (Sprinkler Temperature Ratings and Color Codes) and general principles of sprinkler selection near heat sources."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
