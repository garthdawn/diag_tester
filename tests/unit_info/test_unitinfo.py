import pytest
import allure
from pathlib import Path
from data.test_case_loader import TestCaseLoader

# Load System Cases 
SYSTEM_CASES = TestCaseLoader.load_system_cases_from_json("data/test_cases.json")
SYSTEM_CASE_IDS = [case["name"] for case in SYSTEM_CASES]

class Test_unitinfo:
    def setup_method(self):
        self.card_data = {}
        self.log_content = ""


    def _parse_card_data(self, case):
        command = case["command"],
        expected_output = case.get("expected_output")
        log_file = case["log_file"]

        log_path = Path("results/logs") / log_file
        print(f"log file: {log_path.absolute()}")

        if not log_path.exists():
            pytest.skip(f"log file not exist: {log_path}")
        
        with open(log_path, 'r') as f:
            self.log_content = f.read()
        
        with allure.step(f"commands: {command}"):
            allure.attach(self.log_content, "Unit Response Logs", allure.attachment_type.TEXT)
        
        if expected_output:
            assert expected_output.lower() in log_content.lower(), \
                f"Expected output '{expected_output}' NOT Found in Log"

        line_list = [line.strip() for line in self.log_content.splitlines()]
        if not line_list:
            assert False, "Log file is empty"

        config_start = config_end = 0 
        for i, line in enumerate(line_list):
            if '----' in line: 
                config_start = i
                for j in range(len(line_list)-1, i, -1):
                    if '----' in line_list[j]:
                        config_end = j
                        break
                break

        # print(config_start, config_end)
        for j in range(len(line_list)-1, config_end-1, -1):
            line_list.pop(j)
        for i in range(config_start, -1, -1):
            line_list.pop(i)
        
        # Now line_list is sheer output of slot configuration.
        # Dict Key is slot number, Value is Card Data

        for line in line_list:
            wordlist = line.split()
            if len(wordlist) >= 7 and wordlist[0].isdigit():
                slot = int(wordlist[0])
                card_info = [
                    wordlist[1],  # Card Name
                    wordlist[2],  # Product-ID
                    wordlist[3],  # Serial-No
                    wordlist[4],  # HW Rev
                    wordlist[5],  # IPC
                    wordlist[6]   # Status                
                ]
                self.card_data[slot] = card_info


    @pytest.mark.parametrize(
        "case",
        SYSTEM_CASES,
        ids = SYSTEM_CASE_IDS
    )
    def test_display_slot_info(self, device, case):
        self._parse_card_data(case)

        print(f"{'SLOT':2s}\t{'CARD NAME':15s}\t{'PRODUCT-ID':10s}\t{'SERIAL-NO':15s}\t{'HW REV':5s}\t{'IPC':5s}\t{'STATUS':10s}")
        print(f"{'-'*2}\t{'-'*15}\t{'-'*10}\t{'-'*15}\t{'-'*5}\t{'-'*5}\t{'-'*10}")

        for slot, card_info in self.card_data.items():
            print(
                f"{slot:2d}\t"                 
                f"{card_info[0]:15s}\t"         
                f"{card_info[1]:10s}\t"       
                f"{card_info[2]:15s}\t"       
                f"{card_info[3]:5s}\t"        
                f"{card_info[4]:5s}\t"         
                f"{card_info[5]:10s}"
            )

        assert self.card_data, "There is no Card Info!!!"