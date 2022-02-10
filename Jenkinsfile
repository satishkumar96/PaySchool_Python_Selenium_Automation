pipeline {
    agent any

    stages {
        stage('Clean workspace')
        {
            steps
            {
                cleanWs()
            }
        }
        stage('Build') {
            steps {
               git branch: 'main', url: 'https://github.com/satishkumar96/PaySchool_Python_Selenium_Automation.git'
            }
        }
        stage('Test and emailable report')
        {
            steps
            {
                bat 'pip install -r requirements.txt'
                bat 'pip-review --auto'
                bat 'pytest'
            }

            post
            {

            always
            {
                publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'HTML_Reports', reportFiles: 'AutomationReport.html', reportName: 'AutomationReport', reportTitles: 'PaySchool Automation Report'])
            }

                failure
                    {
                        emailext attachLog: false, attachmentsPattern: 'HTML_Reports/AutomationReport.html', body: '''Hello Everybody,
The execution of PSA Automation Testing in Dev environment has failed. We are looking into the issue and would re-run the automation job upon rectifying the issue.
Regards,
QA Team''', subject: '[$BUILD_STATUS] - $PROJECT_NAME - Build # $BUILD_NUMBER ($BUILD_ID)', to: 'deepakd@chimeratechnologies.com, cc:sk.kumar805@gmail.com'
            }

            success
            {
                emailext attachLog: false, attachmentsPattern: 'HTML_Reports/AutomationReport.html', body: '''Hello Everybody,
The automated test execution of PSA Regression Test Cases is completed. Please find the test report in the below ,
PSC Automation Testing Report - Beta.
Regards,
QA Team''', subject: '[$BUILD_STATUS] - $PROJECT_NAME - Build # $BUILD_NUMBER ($BUILD_ID)', to: 'deepakd@chimeratechnologies.com, cc:sk.kumar805@gmail.com'
            }

            }
        }

            }
        }