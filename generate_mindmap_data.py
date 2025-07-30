import json

input_file_path = "H:\\Google Drive\\MN_SprinklerFitters_Exam\\Grok4 applied corrections.json"
output_file_path = "H:\\Google Drive\\MN_SprinklerFitters_Exam\\docs\\mindmap_data.json"

try:
    with open(input_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    mindmap_root = {
        "id": "root",
        "topic": "Fire Protection Standards Study Guide",
        "children": []
    }

    tag_nodes = {}
    question_counter = 0  # Used to ensure unique IDs for duplicated nodes

    for item in data:
        original_question_id = item['id']  # Preserve original for suffix
        question_topic = item['question']
        answer_topic = item['answer']
        source_info = item.get('source', 'No source provided')

        tags = item.get('tags', []) or ['General']  # Handle untagged as 'General'

        for tag in tags:
            tag_id = f"tag_{tag.replace(' ', '_').replace('-', '_')}"
            if tag_id not in tag_nodes:
                tag_nodes[tag_id] = {
                    "id": tag_id,
                    "topic": tag if tag != 'General' else 'General / Untagged',
                    "children": []
                }
                mindmap_root["children"].append(tag_nodes[tag_id])

            # Create a unique node instance for this tag
            unique_suffix = question_counter
            question_id = f"q_{original_question_id}_{unique_suffix}"
            question_node = {
                "id": question_id,
                "topic": question_topic,
                "children": [
                    {"id": f"a_{original_question_id}_{unique_suffix}", "topic": f"Answer: {answer_topic}"},
                    {"id": f"s_{original_question_id}_{unique_suffix}", "topic": f"Source: {source_info}"}
                ]
            }
            tag_nodes[tag_id]["children"].append(question_node)
            question_counter += 1  # Increment for the next instance

    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(mindmap_root, f, indent=2)

    print(f"Mind map data generated and saved to {output_file_path}")

except FileNotFoundError:
    print(f"Error: The file {input_file_path} was not found.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from {input_file_path}. Check file format.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")