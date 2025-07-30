
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 80:
        item['answer'] = "The required K-factor for sprinklers in rack storage systems varies significantly based on factors such as commodity classification, storage height, and sprinkler type. Specific K-factors are detailed in relevant tables within NFPA 13."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Chapter 21 (Rack Storage) and relevant tables within that chapter."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
