
import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 141:
        item['answer'] = "NFPA 13 does not specify a number of sprinkler heads that triggers the requirement for supervision of control valves. Control valves are generally required to be supervised by an approved method (e.g., central station, proprietary, remote station signaling service, or a local signaling service that sounds an alarm at a constantly attended point)."
        item['source'] = "Authority: NFPA, Document: NFPA 13 2025 Edition, Section: Section 16.9.3 (Supervision of Control Valves)."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
