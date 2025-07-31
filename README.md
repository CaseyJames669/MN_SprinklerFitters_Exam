# MN_SprinklerFitters_Exam

A comprehensive Q&A resource for preparing for the Minnesota Sprinkler Fitters Exam, based on NFPA standards and MN Fire Code. Includes data processing scripts for cleaning, enhancing, and formatting for tools like Quizlet and NotebookLM.

![Repo Badge](https://img.shields.io/github/stars/CaseyJames669/MN_SprinklerFitters_Exam?style=social) ![License](https://img.shields.io/badge/license-MIT-blue)

## Structure
- **data/raw**: Original Q&A JSON/text.
- **data/processed**: Verified and enhanced JSON with corrections.
- **scripts**: Python scripts for processing (e.g., agent.py for full run).
- **outputs**: Formatted TXT for import.
- **docs**: Analysis and mind maps.

## Setup & Usage
1. Clone: `git clone https://github.com/CaseyJames669/MN_SprinklerFitters_Exam.git`
2. Install deps: `pip install -r requirements.txt` (if added; basic stdlib otherwise).
3. Run: `python scripts/agent.py` to process data.
4. Import: Use outputs/ for Quizlet/NotebookLM.

## Visuals
- Mind Map: ![Mind Map](docs/NotebookLM Mind Map.png) – Overview of data flow.
- Web App Screenshot: (Add screenshot of quiz app here – e.g., interactive Q&A interface).

## CI/CD
Pushes trigger GitHub Actions to run verification/tests – see .github/workflows/ci.yml.

## Contributing
See CONTRIBUTING.md.

## License
MIT – see LICENSE.
