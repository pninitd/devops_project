pipeline {
	agent any
	options {
		buildDiscarder(logRotator(numToKeepStr: '20', daysToKeepStr: '5'))
	}
	stages {
		stage('checkout') {
			steps {
				script {
					properties([pipelineTriggers([pollSCM('*/30 * * * *')])])
				}
                // checkout from the url that defined in the jenkins job (git 'https://github.com/pninitd/devops_project.git')
				checkout scm
			}
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
		stage('run backend server') {
			steps {
				script {
					runPythonFileBackground('rest_app.py')
				}
			}
		}
		stage('run frontend server') {
			steps {
				script {
					runPythonFileBackground('web_app.py')
				}
			}
		}
		stage('run backend testing') {
			steps {
				script {
					runPythonFile('backend_testing.py')
				}
			}
		}
		stage('run frontend testing') {
			steps {
				script {
					runPythonFile('frontend_testing.py')
				}
			}
		}
		stage('run combined testing.') {
			steps {
				script {
					runPythonFile('combined_testing.py test')
				}
			}
		}
		stage('run clean environment') {
			steps {
				script {
					runPythonFile('clean_environment.py')
				}
			}
		}
	}
}

def runPythonFile(pyfilename){
	try{
		if (isUnix()) {
			sh "python ${pyfilename}"
		} else {
			bat "python ${pyfilename}"
		}
	} catch (Throwable e) {
		echo "Caught in runPythonFile for ${pyfilename}, ${e.toString()}"
	}
}

def runPythonFileBackground(pyfilename){
	try{
		if (isUnix()) {
			sh "nohup python ${pyfilename} &"
		} else {
			bat "start /min python ${pyfilename}"
		}
	}
	catch (Throwable e) {
		echo "Caught in runPythonFileBackground for ${pyfilename} ${e.toString()}"
	}
}