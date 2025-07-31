import json

input_file_path = "H:\\Google Drive\\MN_SprinklerFitters_Exam\\Grok4 applied corrections.json"

try:
    with open(input_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    source_to_tag_mapping = {
        "NFPA 13D": "NFPA 13D",
        "NFPA 13R": "NFPA 13R",
        "NFPA 17A": "NFPA 17A",
        "NFPA 22": "NFPA 22",
        "NFPA 24": "NFPA 24",
        "NFPA 72": "NFPA 72",
        "NFPA 96": "NFPA 96",
        "MN Statutes": "MN Statutes"
    }

    updated_count = 0
    for item in data:
        if 'source' in item and item['source']:
            for source_key, new_tag in source_to_tag_mapping.items():
                if source_key in item['source']:
                    if 'tags' not in item or item['tags'] is None:
                        item['tags'] = []
                    if new_tag not in item['tags']:
                        item['tags'].append(new_tag)
                        updated_count += 1

    with open(input_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

    print(f"Updated {updated_count} items with new granular tags in {input_file_path}")

except FileNotFoundError:
    print(f"Error: The file {input_file_path} was not found.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from {input_file_path}. Check file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
