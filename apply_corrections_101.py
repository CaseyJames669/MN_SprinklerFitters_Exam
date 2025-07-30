
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 160:
        item['answer'] = "0.75 inches (This is a common minimum pipe size for plastic systems, but specific requirements depend on the system type, occupancy hazard, and manufacturer's listing. Refer to NFPA 13 for detailed tables)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 6.3 (General section on nonmetallic pipe) and relevant tables."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
