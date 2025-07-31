# MN Sprinkler Fitters Exam Study Guide

A comprehensive, scripted dataset of questions and answers for studying for the Minnesota Sprinkler Fitters Exam. This project sources material from NFPA standards and Minnesota state codes, then cleans, processes, and formats it for various study applications, including a web-based quiz app and an interactive mind map.

---

## Project Structure

The repository is organized into the following directories:

- **`/src/`**: Contains the source code for the web application.
- **`/scripts/`**: Houses all Python scripts used for the data processing pipeline.
- **`/data/`**: Contains the JSON data files, separated into `raw/` and `processed/` subdirectories.
- **`/reference/`**: Stores the raw source material, including `nfpa/` and `minnesota/` codes and standards.
- **`/output/`**: Holds the generated output files, such as formatted text for Quizlet or data for the mind map.
- **`/visualization/`**: Contains the HTML, CSS, and JavaScript for the interactive mind map.
- **`/docs/`**: Includes project documentation.
- **`/archive/`**: Stores archived files, such as saved web pages, that are not part of the main data flow but are preserved for reference.

Other important files in the root directory:

- **`JSON Analysis.md`**: A detailed report on the structure, integrity, and quality of the JSON data.

---

## Data Flow & Usage

The project's workflow takes raw data, processes it through a series of Python scripts, and generates clean, usable study guides and applications.

**1. Raw Data:**

- The process starts with the raw data located in `/data/raw/`, primarily `Quizlet Full - Original.json`.

**2. Processing Pipeline:**

- The scripts in the `/scripts/` directory are used to process the raw data. Key scripts include:
  - `format_quizlet.py`: Formats the data for Quizlet.
    - `fix_json.py`, `repair_json.py`, `validate_data.py`: Clean and validate the JSON data.
    - `enhance_json.py`, `extract_tags.py`, `extract_sources.py`: Enrich the data with metadata.
    - `convert_to_notebooklm.py`: Prepares the data for NotebookLM.
    - `generate_mindmap_data.py`: Creates the data for the mind map visualization.

**3. Processed Data & Outputs:**

- The processed and enhanced data is stored in `/data/processed/`. The final, canonical dataset is `Grok4 applied corrections.json`.
- Generated files for specific applications are placed in `/output/`.

**4. Applications:**

- **Web App:** The Flask application in `/src/web_app/` serves the processed data as an interactive quiz.
- **Mind Map:** The files in `/visualization/` create an interactive mind map of the study material.

---

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages (see `requirements.txt`)

### Usage

To run the web application:

```bash
python src/web_app/app.py
```

To regenerate the processed data, run the relevant scripts from the `/scripts/` directory.

---

## Interactive Mind Map

✨ **Explore the dataset interactively as a mind map, hosted on GitHub Pages:**

**[Launch Interactive Mind Map](http.caseyjames669.github.io/MN_SprinklerFitters_Exam/visualization/)**

---
