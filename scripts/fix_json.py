
import os

file_path = 'Quizlet Full - Enhanced.json'

# Read the original file content
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# --- Start of Corrections ---

# 1. Fix known missing commas (e.g., id: 42)
# This is a bit brittle, a more robust regex might be better, but this will work for the known issue.
content = content.replace(
    '"answer": "1\\"/1\\u00bc\\":12\\\'; 1\\u00bd\\"-8\\":15\\'"\n    "source"',
    '"answer": "1\\"/1\\u00bc\\":12\\\'; 1\\u00bd\\"-8\\":15\\'",\n    "source"'
)

# 2. Fix known extraneous characters (e.g., ids: 275, 276, 277, 278)
content = content.replace('12 ft )', '12 ft')
content = content.replace('15 ft )', '15 ft')

# 3. Attempt to fix JSON structure by removing trailing commas in arrays/objects and ensuring it ends correctly
lines = content.split('\n')
cleaned_lines = []
for i, line in enumerate(lines):
    stripped_line = line.strip()
    # Remove trailing commas from lines that are likely the end of a list/object property
    if stripped_line.endswith(',') and i + 1 < len(lines) and lines[i + 1].strip() in (']', '}'):
        cleaned_lines.append(line.rstrip().rstrip(','))
    else:
        cleaned_lines.append(line)

content = '\n'.join(cleaned_lines)

# 4. Ensure the file starts with '[' and ends with ']'
if not content.strip().startswith('['):
    content = '[' + content
if not content.strip().endswith(']'):
    # Find the last valid closing brace and append the closing bracket after it
    last_brace_index = content.rfind('}')
    if last_brace_index != -1:
        # Check if there's a comma after the last brace that needs to be removed
        if content[last_brace_index+1:].strip().startswith(','):
            content = content[:last_brace_index+1] + content[last_brace_index+1:].replace(',', '', 1)
        content = content[:last_brace_index+2] + '\n]' + content[last_brace_index+2:]
    else: # Fallback if no brace is found
        content = content.strip() + '\n]'

# Write the corrected content back to the file
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"File '{file_path}' has been cleaned and corrected.")
