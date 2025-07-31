

import os
import shutil

# Define the root directory (where the script is located)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define the new directory structure
DIRS_TO_CREATE = [
    "archive",
    "data/raw",
    "data/processed",
    "docs",
    "output",
    "reference/minnesota",
    "reference/nfpa",
    "scripts",
    "src",
    "visualization"
]

# --- Mapping of files to their new homes ---
# Format: "destination_directory": ["file_or_folder_1", "file_or_folder_2", ...]
FILE_MAP = {
    "scripts": [
        "add_granular_tags.py", "apply_corrections.py", "convert_to_notebooklm.py",
        "create_nfpa_corpus.py", "enhance_json.py", "extract_sources.py",
        "extract_tags.py", "fix_json_again.py", "fix_json.py", "format_quizlet.py",
        "generate_mindmap_data.py", "process_json.py", "rebuild_data.py",
        "repair_json.py", "validate_data.py"
    ],
    "data/raw": [
        "Quizlet Full - Original.json",
        "Quizlet Full - Original.txt"
    ],
    "data/processed": [
        "nfpa_corpus.json",
        "Quizlet Full - Enhanced.json",
        "Quizlet Full - Verified.json",
        "Grok4 accuracy verification results.json",
        "Grok4 applied corrections.json"
    ],
    "output": [
        "Quizlet Full - FormattedForImport.txt",
        "Quizlet Full - NotebookLM.txt",
        "mindmap_data.json",
        "Full Summary Table for Grok4_Quizlet Full - Enhanced.csv"
    ],
    "visualization": [
        "index.html",
        "mindmap.js",
        "NotebookLM Mind Map.png",
        "docs" # This is the docs folder from the root
    ],
    "archive": [
        "The National Fire Codes Subscription Service - NFPA 13_ Standard for the Installation of Sprinkler Systems, 2019 Edition.html",
        "The National Fire Codes Subscription Service - NFPA 13_ Standard for the Installation of Sprinkler Systems, 2019 Edition_files"
    ],
    "reference/minnesota": [
        "MN Stuff"
    ],
    "reference/nfpa": [
        "NFPAs"
    ],
    "src": [
        "web_app"
    ],
    "docs": [
        "commit_message.txt",
        "JSON Analysis.md"
    ]
}

def organize_repo():
    """Creates directories and moves files according to the plan."""
    print("Starting repository reorganization...")

    # 1. Create all necessary directories
    for d in DIRS_TO_CREATE:
        path = os.path.join(ROOT_DIR, d)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Created directory: {path}")

    # 2. Move files and directories
    for dest, items in FILE_MAP.items():
        dest_path = os.path.join(ROOT_DIR, dest)
        for item in items:
            src_path = os.path.join(ROOT_DIR, item)
            
            # Handle special cases for MN Stuff and NFPAs content
            if item in ["MN Stuff", "NFPAs"]:
                # Move the *contents* of the folder
                final_dest = os.path.join(ROOT_DIR, dest, os.path.basename(item).lower())
                if not os.path.exists(final_dest):
                    os.makedirs(final_dest)

                for content_item in os.listdir(src_path):
                    content_src = os.path.join(src_path, content_item)
                    content_dest = os.path.join(final_dest, content_item)
                    if os.path.exists(content_src):
                        shutil.move(content_src, content_dest)
                        print(f"Moved {content_src} -> {content_dest}")
                # Remove the now-empty source directory
                if os.path.exists(src_path):
                    shutil.rmtree(src_path)
                    print(f"Removed directory (and its contents): {src_path}")
            else:
                # Standard file/folder move
                if os.path.exists(src_path):
                    try:
                        shutil.move(src_path, dest_path)
                        print(f"Moved {item} -> {dest}")
                    except Exception as e:
                        print(f"Could not move {item}. Reason: {e}")
                else:
                    print(f"Skipping {item}, does not exist at root.")

    print("\nReorganization complete!")
    print("Please check your version control status and test application functionality.")

if __name__ == "__main__":
    organize_repo()
