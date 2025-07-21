import os
import pytest
import allure
import datetime
from pathlib import Path
from lib.device import Device

def find_txt_files(root_dir):
    txt_files = []
    
    for root, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                txt_files.append(file_path)
    
    return txt_files

def file_in_time_range(filepath_list, start_time, end_time):
    """start_time和end_time都需要是datetime格式"""
    time_match_file_list = []
    
    for filepath in filepath_list:
        creation_time = os.path.getmtime(filepath)
        if creation_time is not None: 
            file_time = datetime.datetime.fromtimestamp(creation_time)
            # 从datetime转换成timestamp: datetime.datetime.timestamp(file_time)
            # print(f"{creation_time} == {file_time}")
            if start_time <= file_time <= end_time: 
                time_match_file_list.append([filepath, file_time.strftime("%Y年%m月%d日 %H:%M:%S")])

    return time_match_file_list


class Test_unit_log_file:
    def setup_method(self):
        self.file_list_in_range = []
        self.root_dir = Path("results/log_files")

    @pytest.mark.parametrize(
        "start_time, end_time",
        [
            (
                datetime.datetime.now() - datetime.timedelta(days=1),
                datetime.datetime.now(),
            ),
            (
                datetime.datetime.now() - datetime.timedelta(days=5),
                datetime.datetime.now(),
            ),
        ],
        ids = ["files of today", "files within 5 days"]
    )    
    
    def test_find_log_in_time_range(self, device, start_time, end_time):

        with allure.step(f"Step1: Find all txt files under target folder"):
            txt_files_list = find_txt_files(self.root_dir)
            file_names = "\n".join(txt_files_list)

            allure.attach(
                f"find {len(txt_files_list)} TXT files, \
                the names are: {file_names}",
                name = "Find all txt files",
                attachment_type = allure.attachment_type.TEXT
                )
        
        with allure.step(f"Step2: filter files from {start_time} to {end_time}"):
            self.file_list_in_range = file_in_time_range(txt_files_list, start_time, end_time)
            result = "\n".join(self.file_list_in_range)
            print(result)

            allure.attach(
                result,
                name="",
                attachment_type = allure.attachment_type.TEXT
            )

        with allure.step(f"Step3: Assert whether target file is found."):
            assert True