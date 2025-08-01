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
   
## Webhook is effective. 
1. Once a Merge has been made to https://github.com/garthdawn/diag_tester. A jenkins test job will be auto triggered. 
2. The jenkins job can be seen in : https://762b73abb6b5.ngrok-free.app/job/diag-tester-mr/ 
   (this is a global hostname of my local Jenkins server, realized by ngrok,
      it will not be accessible if my laptop is offline)