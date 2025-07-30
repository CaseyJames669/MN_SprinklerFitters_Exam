
import json

def fix_json_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    corrected_lines = []
    for line in lines:
        # Add comma between tags
        if '"NFPA-25"' in line and '"Water-Supply"' in line:
            line = line.replace('"NFPA-25"\n      "Water-Supply"', '"NFPA-25",\n      "Water-Supply"')
        if '"NFPA-13R"' in line and '"Sprinklers-Types"' in line:
            line = line.replace('"NFPA-13R"\n      "Sprinklers-Types"', '"NFPA-13R",\n      "Sprinklers-Types"')
        if '"Hazard-Classification"' in line and '"NFPA-13"' in line:
            line = line.replace('"Hazard-Classification"\n      "NFPA-13"', '"Hazard-Classification",\n      "NFPA-13"')
        if '"NFPA-13"' in line and '"Sprinklers"' in line:
            line = line.replace('"NFPA-13"\n      "Sprinklers"', '"NFPA-13",\n      "Sprinklers"')
        if '"Sprinklers"' in line and '"Sprinklers-Spacing"' in line:
            line = line.replace('"Sprinklers"\n      "Sprinklers-Spacing"', '"Sprinklers",\n      "Sprinklers-Spacing"')

        # Add comma between answer and source for id 42
        if '"answer": "1\"/1\\u00bc\\\":12\\\'; 1\\u00bd\\\"-8\\\":15\\\'"' in line:
            line = line.replace('"answer": "1\"/1\\u00bc\\\":12\\\'; 1\\u00bd\\\"-8\\\":15\\\'"',
                            '"answer": "1\"/1\\u00bc\\\":12\\\'; 1\\u00bd\\\"-8\\\":15\\\'",')

        # Remove extraneous characters from answers
        if '12 ft )' in line:
            line = line.replace('12 ft )', '12 ft')
        if '15 ft )' in line:
            line = line.replace('15 ft )', '15 ft')

        corrected_lines.append(line)

    # Add missing closing bracket
    if not corrected_lines[-1].strip() == ']':
        corrected_lines.append(']')

    with open(file_path, 'w') as f:
        f.writelines(corrected_lines)

if __name__ == '__main__':
    fix_json_file('Quizlet Full - Enhanced.json')
    print("JSON fix script complete.")
