import pytest
import json
from scripts.process_json import deduplicate  # Assume function name; adjust as needed

sample_data = [
    {"question": "Q1", "answer": "A1"},
    {"question": "Q1", "answer": "A1"},  # Duplicate
    {"question": "Q2", "answer": "A2"}
]

def test_deduplicate():
    unique = deduplicate(sample_data)
    assert len(unique) == 2
    assert unique[0]["question"] == "Q1"
    assert unique[1]["question"] == "Q2"

# Add more tests for enhancement, formatting, etc.
