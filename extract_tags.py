import json

input_file_path = "H:\\Google Drive\\MN_SprinklerFitters_Exam\\Grok4 applied corrections.json"

try:
    with open(input_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    unique_tags = set()
    for item in data:
        if 'tags' in item and item['tags']:
            for tag in item['tags']:
                unique_tags.add(tag)

    sorted_tags = sorted(list(unique_tags))

    print("Extracted Unique Tags:")
    for tag in sorted_tags:
        print(f"- {tag}")

except FileNotFoundError:
    print(f"Error: The file {input_file_path} was not found.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from {input_file_path}. Check file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

