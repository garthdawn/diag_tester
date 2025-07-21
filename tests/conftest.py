import os
import json
import pytest
import allure
from pathlib import Path
from datetime import datetime

from lib.device import Device

@pytest.fixture(scope="function")
def device():
    """initialize the device under test """

    dev = Device(model= "mds_9509", ip="172.20.10.5", baud_rate = 9600)
    print(f"initialize device: {dev.model}, (IP = {dev.ip}, baud_rate = {dev.baud_rate})")

    with allure.step("Device Power On"):
        power_result = dev.power_on()
        assert "successfully" in power_result, "Device Power On Failed"

    with allure.step("Serial Connect"):
        serial_result = dev.serial_connect()
        assert serial_result, "Serial Connect Failed"

    with allure.step("boot into ROMMON"):
        rommon_prompt = dev.press_break_key()
        assert "rommon 1 >" in rommon_prompt, "Failed to boot into Rommon"
        assert dev.rommon_mode, "Not Set Rommon Flag"

    with allure.step("Boot inti Diag Image"):
        diag_result = dev.enter_diag_mode()
        assert "Diagnostic mode enabled" in diag_result, "Failed to boot into Diag"
        assert dev.diag_mode, "Not Set Diag Flag"

    yield dev
    
    with allure.step("End Test, clear resources"):
        print(f"\nEnding, clear resources {dev.model}")
        dev.ssh_connected = False
        dev.powered_on = False

# # read test case info from json file
# @pytest.fixture(scope="session")
# def test_suite():
#     with open(Path("data/test_cases.json")) as f:
#         return json.load(f)

# @pytest.fixture(scope="session")
# def test_cases(test_suite):
#     return test_suite["test_cases"]

# # generate ids list
# @pytest.fixture(scope="session")
# def test_case_ids(test_cases):
#     return [case["name"] for case in test_cases]


def pytest_sessionfinish(session: pytest.Session, exitstatus: int):
    """Print Allure Report Link after test complete"""
    allure_dir = session.config.getoption("--alluredir")
    
    if allure_dir:

        if os.path.exists(allure_dir):
            print("\n" + "="*50)
            print(f"Allure Report is in: {os.path.abspath(allure_dir)}")
            print(f"First execute: allure serve {allure_dir}")
            print(f"then the report link appears and you can check.")
            print("="*50 + "\n")
        else:
            print(f"\n警告: Allure Report Not Exist - {allure_dir}")