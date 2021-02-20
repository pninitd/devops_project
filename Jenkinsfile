pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('* * * * *')])])
                }
                git 'https://github.com/Dgotlieb/JenkinsTest.git'
            }
        }
        stage('run python') {
            steps {
                script {
                    if (Boolean.valueOf(env.UNIX)) {
                        sh 'python 1.py'
                    } else {
                        bat 'python 1.py'
                    }
                }
            }
        }
    }
}