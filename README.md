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
   
## Local Jenkins Server is ready.
1. install jenkins tool sets locally, and launch properly 
   (I did in Macolder version, while it's easier in Ubuntu)
2. in Jenkins - management page, install plugins:
         Git Plugin
         Pipeline Plugin
         Allure Plugin
         GitHub Plugin
3. set Allure commandline : install automatically.
   SCM : input https://github.com/garthdawn/diag_tester.git
   script path: pipeline/Jenkinsfile

4. then can access jenkins page: http://localhost:8080/job/diag-tester-mr/
   and start test job, job will end with proper Allure report.