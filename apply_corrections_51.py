import json

file_path = r'C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Enhanced.json'

# Load the JSON data
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Apply corrections
for item in data:
    if item['id'] == 82:
        item['answer'] = "The center of the four-inch (4\") port of a fire hydrant must be a minimum of twenty-four inches (24\") above the finished grade."
        item['source'] = "Authority: MN, Document: State Fire Code, Section: Chapter 5."

# Save the corrected JSON data back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print("Corrections applied.")
