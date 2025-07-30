# Fire Protection Standards Study Guide

A comprehensive, scripted dataset of questions and answers for studying fire protection standards, primarily sourced from NFPA codes. This project cleans, enhances, and formats study materials for various applications like Quizlet and Google's NotebookLM.

---

## AI-Enhanced Version (July 29, 2025)

- Used Grok 4 AI agent for 100% accuracy verification against NFPA 2025 and MN Fire Code.
- **Grok4 applied corrections.json** is now the final, corrected dataset.
- New features: PDF study guide, web quiz app, expanded Q&A.
- Run `python agent.py` to regenerate.

## Key Features

- **Comprehensive Dataset**: A large collection of Q&A pairs covering critical fire protection topics.
- **Standardized Sources**: Each entry is linked to a specific code section, with sources formatted as `Authority: [Name], Document: [Title], Section: [Number]`.
- **Automated Processing**: Python scripts to clean, verify, and enhance the dataset for consistency and accuracy.
- **Multiple Formats**: Data is available in raw, cleaned, and enhanced JSON, plus text formats optimized for different study platforms.
- **Unique IDs**: Every Q&A pair has a unique `id` for easy referencing.
- **Granular Tagging**: A hierarchical tagging system (e.g., `Piping-Materials`, `System-Components`) allows for more precise content filtering.
- **Structured Answers**: Complex answers with lists or key-value pairs are automatically converted into structured JSON objects for easier programmatic access.

---

## Project Structure and Data Flow

The project revolves around taking a raw JSON dataset and processing it through a series of scripts to produce clean, enhanced, and usable study guides. This workflow is visualized below:

![Project Data Flow](NotebookLM%20Mind%20Map.png)

### Interactive Mind Map

Explore the dataset interactively as a mind map, hosted on GitHub Pages:

[Launch Interactive Mind Map](https://<YOUR_USERNAME>.github.io/<YOUR_REPOSITORY_NAME>/docs/)

### File Descriptions

#### 🗂️ Data Files

- **`Quizlet Full - Original.json`**: The raw, unprocessed data. Contains potential duplicates and formatting inconsistencies.
- **`Quizlet Full - Original.txt`**: The raw, unprocessed data in plain text format.
- **`Quizlet Full - Verified.json`**: The cleaned version of the data, with duplicates removed.
- **`Quizlet Full - Enhanced.json`**: The most advanced dataset. Includes a unique `id`, standardized `source`, granular `tags`, and structured `answer` fields.
- **`Grok4 accuracy verification results.json`**: The dataset used for Grok 4 AI agent verification, containing original data and correction suggestions.
- **`Grok4 applied corrections.json`**: The final, corrected dataset after applying Grok 4 AI agent verification results.
- **`Quizlet Full - FormattedForImport.txt`**: A text version of the data, formatted for direct import into Quizlet.
- **`Quizlet Full - NotebookLM.txt`**: A plain text version of the enhanced data, specifically formatted for use as a source in Google's NotebookLM.

#### ⚙️ Python Scripts

- **`process_json.py`**: Reads `Quizlet Full - Original.json`, removes duplicate questions, and saves the result as `Quizlet Full - Verified.json`.
- **`enhance_json.py`**: Takes the verified data, adds detailed `tags` and `source` fields to each entry, and applies Markdown formatting. Saves the result as `Quizlet Full - Enhanced.json`.
- **`convert_to_notebooklm.py`**: Converts the final enhanced JSON into the `Quizlet Full - NotebookLM.txt` format.
- **`format_quizlet.py`**: Formats the verified JSON data into a tab-separated text file (`Quizlet Full - FormattedForImport.txt`) suitable for Quizlet import.

#### 📄 Documentation

- **`JSON Analysis.md`**: A detailed report on the structure, integrity, and quality of the JSON data, including suggestions for improvement.
- **`NotebookLM Mind Map.pdf` / `.png`**: Visual diagram of the project's file structure and data flow.
- **`NotebookLM Audio Overview.wav`**: An audio recording providing an overview of the project's integration with Google's NotebookLM.

---

## Getting Started

### Prerequisites

- Python 3.x

### Usage

To regenerate all processed files from the original data, simply run the `agent.py` script:

```bash
python agent.py
```

This single command will handle all the processing steps, including deduplication, verification (if an API key is provided), enhancement, and generation of all output files.

---

## Data Sources

The study material is primarily sourced from the following standards:

- NFPA 13, 2025 Edition
- NFPA 13D, 2022 Edition
- NFPA 13R, 2022 Edition
- NFPA 14, 2022 Edition
- NFPA 17A, 2024 Edition
- NFPA 20, 2022 Edition
- NFPA 22, 2023 Edition
- NFPA 24, 2022 Edition
- NFPA 25, 2023 Edition
- NFPA 72, 2024 Edition
- NFPA 96, 2024 Edition
- Minnesota State Fire Code, 2020
- MN Statutes

---

## Future Improvements


- **Web Interface for Data Exploration**: Create a simple web application to browse, search, and filter the Q&A dataset.
- **Automated Data Validation and Cleaning**: Implement a more robust data validation pipeline to automatically detect and flag inconsistencies.
- **Expand the Dataset with More Sources**: Incorporate additional fire protection standards, such as those from the International Building Code (IBC).
- **Advanced Data Analysis and Insights**: Develop scripts to analyze the dataset for trends and insights.
- **Interactive Quiz Feature**: Build a command-line or web-based quiz tool that pulls questions from the dataset and tests the user's knowledge.