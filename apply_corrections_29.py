
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 49:
        item['answer'] = "Sprinklers located above heat ducts or other heat sources should have a temperature rating appropriate for the maximum ambient ceiling temperature, typically at least 20°F (11°C) above it. This often requires intermediate or high-temperature sprinklers depending on the proximity and nature of the heat source."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 7.3.2 (Sprinkler Temperature Ratings) and general principles of sprinkler selection near heat sources."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
