# Quizlet Study Files

This directory contains several JSON files designed for studying fire protection standards, along with the Python scripts used to process them.

---

### JSON Data Files

*   **`Quizlet Full - Original.json`**: The raw, unprocessed data as it was initially provided. This file may contain errors, duplicate entries, and malformed data.

*   **`Quizlet Full - Verified.json`**: A cleaned and verified version of the original data, specifically formatted for use with [Quizlet](https://quizlet.com). This version is ideal for direct import into Quizlet, which has a two-column (e.g., term and definition) import limit.

*   **`Quizlet Full - Enhanced.json`**: The most advanced version of the data, designed for more flexible and powerful study applications. It includes additional fields for `source` and `tags`, and the `answer` field is formatted with Markdown for better readability.

### Text File

*   **`Quizlet Full - Original.txt`**: The original data in a plain text format.

### Python Scripts

*   **`process_json.py`**: This script was used to clean the `Quizlet Full - Original.json` file by removing duplicate questions and a malformed entry at the end of the file. The output of this script is `Quizlet Full - Verified.json`.

*   **`enhance_json.py`**: This script takes the `Quizlet Full - Verified.json` file and enhances it by adding `tags` and a separate `source` field for each entry, and by formatting answers with Markdown. The output of this script is `Quizlet Full - Enhanced.json`.