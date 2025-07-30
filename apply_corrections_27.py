
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 47:
        item['answer'] = "Within 24 inches (This is a common industry practice for providing support close to changes in direction or connections, though a specific section for this exact distance on horizontal mains after a riser is not explicitly detailed in publicly available NFPA 13 2025 summaries outside of seismic bracing)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: General principles of hanger spacing and support (refer to Chapter 17 for general hanger requirements)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
