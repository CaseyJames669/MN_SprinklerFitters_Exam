import json

def repair_json_file(file_path):
    repaired_lines = []
    with open(file_path, 'r') as f:
        lines = f.readlines()

    for line in lines:
        # Attempt to fix the most common error: trailing commas
        line = line.strip()
        if line.endswith(','):
            try:
                json.loads(line[:-1])
                repaired_lines.append(line[:-1])
                continue
            except json.JSONDecodeError:
                pass
        repaired_lines.append(line)

    # Re-assemble the JSON file
    full_repaired_json = '\n'.join(repaired_lines)

    # Add the missing closing bracket
    if not full_repaired_json.strip().endswith(']'):
        full_repaired_json += '\n]'

    with open(file_path, 'w') as f:
        f.write(full_repaired_json)

if __name__ == '__main__':
    repair_json_file('Quizlet Full - Enhanced.json')
    print("JSON repair complete.")
