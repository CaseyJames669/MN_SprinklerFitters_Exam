# Fire Protection Standards Study Guide

A comprehensive, scripted dataset of questions and answers for studying fire protection standards, primarily sourced from NFPA codes. This project cleans, enhances, and formats study materials for various applications like Quizlet and Google's NotebookLM.

---

## Key Features

- **Comprehensive Dataset**: A large collection of Q&A pairs covering critical fire protection topics.
- **Verified Sources**: Each entry is linked to a specific code section from major NFPA standards and other official sources.
- **Automated Processing**: Python scripts to clean, verify, and enhance the dataset for consistency and accuracy.
- **Multiple Formats**: Data is available in raw, cleaned, and enhanced JSON, plus text formats optimized for different study platforms.

---

## Project Structure and Data Flow

The project revolves around taking a raw JSON dataset and processing it through a series of scripts to produce clean, enhanced, and usable study guides. This workflow is visualized below:

![Project Data Flow](NotebookLM%20Mind%20Map.png)

### File Descriptions

#### 🗂️ Data Files

-   **`Quizlet Full - Original.json`**: The raw, unprocessed data. Contains potential duplicates and formatting inconsistencies.
-   **`Quizlet Full - Verified.json`**: The cleaned version of the data, with duplicates removed. Ideal for direct import into Quizlet (term/definition format).
-   **`Quizlet Full - Enhanced.json`**: The most advanced dataset. Includes distinct `source` and `tags` fields, with Markdown formatting in the `answer` field for improved readability.
-   **`Quizlet Full - NotebookLM.txt`**: A plain text version of the enhanced data, specifically formatted for use as a source in Google's NotebookLM.

#### ⚙️ Python Scripts

-   **`process_json.py`**: Reads `Quizlet Full - Original.json`, removes duplicate questions, and saves the result as `Quizlet Full - Verified.json`.
-   **`enhance_json.py`**: Takes the verified data, adds detailed `tags` and `source` fields to each entry, and applies Markdown formatting. Saves the result as `Quizlet Full - Enhanced.json`.
-   **`convert_to_notebooklm.py`**: Converts the final enhanced JSON into the `Quizlet Full - NotebookLM.txt` format.

#### 📄 Documentation

-   **`JSON Analysis.md`**: A detailed report on the structure, integrity, and quality of the JSON data, including suggestions for improvement.
-   **`NotebookLM Mind Map.pdf` / `.png`**: Visual diagram of the project's file structure and data flow.

---

## Getting Started

### Prerequisites

-   Python 3.x

### Usage

To regenerate the processed files from the original data, run the scripts in the following order.

1.  **Clean the original data:**
    This script creates the `Quizlet Full - Verified.json` file.
    ```bash
    python process_json.py
    ```

2.  **Enhance the cleaned data:**
    This script uses the verified file to create the `Quizlet Full - Enhanced.json` file.
    ```bash
    python enhance_json.py
    ```

3.  **Convert for NotebookLM:**
    This script creates the `Quizlet Full - NotebookLM.txt` file from the enhanced data.
    ```bash
    python convert_to_notebooklm.py
    ```

---

## Data Sources

The study material is primarily sourced from the following standards:

-   NFPA 13, 2025 Edition
-   NFPA 13D, 2022 Edition
-   NFPA 13R, 2022 Edition
-   NFPA 14, 2022 Edition
-   NFPA 17A, 2024 Edition
-   NFPA 20, 2022 Edition
-   NFPA 22, 2023 Edition
-   NFPA 24, 2022 Edition
-   NFPA 25, 2023 Edition
-   NFPA 72, 2024 Edition
-   NFPA 96, 2024 Edition
-   Minnesota State Fire Code, 2020
-   MN Statutes

---

## Future Improvements

Based on the analysis in `JSON Analysis.md`, the following enhancements could further improve the dataset:

-   **Standardize `source` Field**: Adopt a consistent format for non-NFPA sources (e.g., `"Authority: [Name], Document: [Title], Section: [Number]"`).
-   **Refine `tags`**: Implement a more granular tagging system, such as using sub-topics like `Piping-Materials` or `Hangers`.
-   **Structure Complex `answer` Fields**: For answers containing lists or multiple conditions, convert the string into a JSON array or object to improve programmatic access.
-   **Add Unique IDs**: Introduce a unique `id` field for each Q&A object to make referencing easier.