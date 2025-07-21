# lib/test_case_loader.py
import json
from pathlib import Path

class TestCaseLoader:
    @staticmethod
    def load_test_cases_from_json(json_path):
        json_path = Path(json_path)
        if not json_path.exists():
            raise FileNotFoundError(f"Test Case File Not Exist: {json_path}")
        
        with open(json_path, "r") as f:
            test_suite = json.load(f)
        
        return test_suite.get("test_cases", [])

    def load_system_cases_from_json(json_path):
        json_path = Path(json_path)
        if not json_path.exists():
            raise FileNotFoundError(f"Test Case File Not Exist: {json_path}")
        
        with open(json_path, "r") as f:
            test_suite = json.load(f)
        
        return test_suite.get("system_cases", [])