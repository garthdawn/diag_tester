import time
import random
from data.test_case_loader import TestCaseLoader

TEST_CASES = TestCaseLoader.load_test_cases_from_json("data/test_cases.json")
TEST_CASE_CMDS = [case["command"] for case in TEST_CASES]

class Device:
    def __init__(self, model: str, ip: str = "172.20.10.5", baud_rate: int = 9600):
        self.ip = ip
        self.model = model
        self.baud_rate = baud_rate
        self.powered_on = False
        self.rommon_mode = False
        self.diag_mode = False
        self.ios_mode = False
        self.ssh_connected = False
        
    def power_on(self) -> str:
        """simulate turn on power relay"""
        self.powered_on = True
        print("Power Relay Turned On, Unit is powering on")
        time.sleep(1)
        return "Unit powered on successfully"
    
    def ping(self, count: int = 5, timeout: int = 5) -> bool:
        if not self.powered_on:
            print("device not powered on")
            return False
        
        print(f"Pinging {self.ip} (count: {count}, timeout: {timeout}s)...")
        return True

    def ssh_connect(
            self, 
            username: str = "admin", 
            password: str = "admin", 
            max_attempts: int = 3, 
            timeout: int = 5
        ):
        if not self.ping(count = 5):
            print("Ping failed, exit")
            return False

        print(f"Try ssh to {self.ip} for {max_attempts} attempts...")
        self.ssh_connected = True 
    
    def serial_connect(self) -> bool:
        print(f"Connecting to serial port at {self.baud_rate} baud...")
        time.sleep(1)
        
        retry = 0
        # 模拟串口连接结果
        while retry < 3:
            if random.random() > 0.9:
                print("Serial connection failed")
                retry += 1
            else:
                print("Serial connection passed")
                break
        return True if retry < 3 else False

    def press_break_key(self):
        """pressing the break key to enter ROMmon mode"""
        self.rommon_mode = True
        return "rommon 1 >"
    
    def enter_diag_mode(self):
        """Enter diagnostic mode from ROMmon"""
        if not self.rommon_mode:
            raise RuntimeError("Device not in ROMmon mode")
        self.diag_mode = True
        self.rommon_mode = False
        return "Diagnostic mode enabled"
    
    def send_command_sync(self, command: str, timeout: int = 10, expected_prompt: str = "]#"):
        """Execute a diagnostic command and return simulated output"""
        if not self.diag_mode:
            raise RuntimeError("Device not in diagnostic mode")
        
        print(f"simulate send command {command} with timeout {timeout}")
        # self.serial_conn.write(f"{command}\r\n".encode())
        # while time.time() - start_time < timeout:
        #     read_data = self.serial_conn.read(1).decode(errors="ignore")  # 逐字节读取
        #     if not read_data:
        #         continue

        return True
        
