import json

input_file_path = "H:\\Google Drive\\MN_SprinklerFitters_Exam\\Grok4 applied corrections.json"

try:
    with open(input_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    unique_sources = set()
    for item in data:
        if 'source' in item and item['source']:
            unique_sources.add(item['source'].split(', ')[0]) # Extract the main source part
        elif 'tags' in item and item['tags']:
            for tag in item['tags']:
                unique_sources.add(tag) # Add tags as sources if no specific source is present

    sorted_sources = sorted(list(unique_sources))

    print("Extracted Sources:")
    for source in sorted_sources:
        print(f"- {source}")

except FileNotFoundError:
    print(f"Error: The file {input_file_path} was not found.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from {input_file_path}. Check file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
