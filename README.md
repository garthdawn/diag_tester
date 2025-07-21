# Simulating Diag Test Framework

## Setup

1. Clone the repository
2. Run the quickstart script:
   ```bash
   chmod +x quickstart.sh
   ./quickstart.sh
3. send test command: pytest tests/ -sv --alluredir=reports/allure-reports
   a total of 5 test cases will be executed. 
4. how to check allure report:
   cd reports
   allure serve allure-reports (then a webpage will prompt up)
   