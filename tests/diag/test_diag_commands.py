import pytest
import allure
from pathlib import Path
from data.test_case_loader import TestCaseLoader
from lib.device import Device

# Load Test Cases
TEST_CASES = TestCaseLoader.load_test_cases_from_json("data/test_cases.json")
TEST_CASE_IDS = [case["name"] for case in TEST_CASES]

@allure.story("Diagnostic Command Tests")
class TestDiagnosticCommands:

    @pytest.mark.parametrize(
        "case",
        TEST_CASES,
        ids=TEST_CASE_IDS
    )
    def test_diagnostics_command(self, device, case):
        command = case["command"]
        expected_output = case.get("expected_output")
        log_file = case["log_file"]
        
        log_path = Path("results/logs") / log_file  
        print(f"\log file : {log_path.absolute()}")  

        if not log_path.exists():
            pytest.skip(f"log file not exist: {log_path}")
        log_content = log_path.read_text()
        
        with allure.step(f"commands: {command}"):
            allure.attach(log_content, "Unit Response Logs", allure.attachment_type.TEXT)
        
        if expected_output:
            assert expected_output.lower() in log_content.lower(), \
                f"Expected output '{expected_output}' NOT Found in Log"
        