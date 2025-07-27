import json

input_file = r"C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - Verified.json"
output_file = r"C:\Users\casey\Github\MN_SprinklerFitters_Exam\Quizlet Full - FormattedForImport.txt"
term_definition_separator = "****"
card_separator = "\n\n"

try:
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    formatted_cards = []
    for item in data:
        term = item.get("question", "").strip()
        definition = item.get("answer", "").strip()
        if term and definition:
            formatted_cards.append(f"{term}{term_definition_separator}{definition}")

    output_content = card_separator.join(formatted_cards)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_content)

    print(f"Successfully formatted and saved to {output_file}")

except FileNotFoundError:
    print(f"Error: Input file not found at {input_file}")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from {input_file}. Please ensure it's valid JSON.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
