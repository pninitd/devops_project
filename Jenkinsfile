pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/pninitd/devops_project.git'
            }
        }
        stage('run python') {
            steps {
                script {
//                  sh 'python1.py'
                    echo "pninit"
                }
            }
        }
    }
}