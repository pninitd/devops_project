pipeline {
    agent any
    options {
        buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
    }
    stage('install missing dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'pip install flask werkzeug requests selenium pymysql -t ./'
                    } else {
                        bat 'pip install flask werkzeug requests selenium pymysql -t ./'
                    }
                }
            }
        }
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
                }
                git 'https://github.com/pninitd/devops_project.git'
            }
        }
        stage('run backend server') {
            steps {
                script { if (isUnix()) {
                        sh 'nohup python rest_app.py &'
                    } else {
                        bat 'start /min python rest_app.py'
                    }
                }
            }
        }
        stage('run frontend server') {
            steps {
                script { if (isUnix()) {
                        sh 'nohup python web_app.py &'
                    } else {
                        bat 'start /min python web_app.py'
                    }
                }
            }
        }
        stage('run backend testing') {
            steps {
                script { if (isUnix()) {
                        sh 'nohup python backend_testing.py &'
                    } else {
                        bat 'start /min backend_testing.py'
                    }
                }
            }
        }
        stage('run frontend testing') {
            steps {
                script { if (isUnix()) {
                        sh 'nohup python frontend_testing.py &'
                    } else {
                        bat 'start /min frontend_testing.py'
                    }
                }
            }
        }
        stage('run combined testing.') {
            steps {
                script { if (isUnix()) {
                        sh 'nohup python combined_testing.py &'
                    } else {
                        bat 'start /min combined_testing.py'
                    }
                }
            }
        }
        stage('run clean environment') {
            steps {
                script { if (isUnix()) {
                        sh 'nohup python clean_environment.py &'
                    } else {
                        bat 'start /min clean_environment.py'
                    }
                }
            }
        }
    }
}