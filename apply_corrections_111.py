
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 173:
        item['answer'] = "Sprinkler temperature ratings are based on the maximum ambient ceiling temperature, not water temperature. If ambient temperatures exceed 100°F (38°C), intermediate or high-temperature sprinklers are typically required."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 7.3.2 (Sprinkler Temperature Ratings) and general principles of sprinkler selection."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
