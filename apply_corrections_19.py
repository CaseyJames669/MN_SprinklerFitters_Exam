import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 38:
        item['answer'] = "Generally, yes, FDCs are required for NFPA 13R systems. NFPA 13R applies to residential occupancies up to and including four stories in height. There is no specific exception for single-story buildings within NFPA 13R regarding FDC requirements. (NFPA 13D, for one- and two-family dwellings, does not require an FDC)."
        item['source'] = "Authority: NFPA, Document: NFPA 13R 2022 Edition, Section: General requirements for FDCs (specific section not explicitly stated in public summaries, but implied by scope) and comparison with NFPA 13D."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")