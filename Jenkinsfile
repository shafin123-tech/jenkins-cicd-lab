
pipeline {
    agent {
        label 'python'
    }

    stages {
        stage('Verify Agent') {
            steps {
                sh 'echo "Hello from Jenkins Agent!"'
                sh 'hostname'
                sh 'pwd'
            }
        }

        stage('Verify Build Environment') {
            steps {
                sh 'python3 --version'
                sh 'pip3 --version'
                sh 'whoami'
            }
        }

        stage('Prepare Environment') {
            steps {
                sh 'python3 -m venv --clear .venv'
                sh '.venv/bin/python --version'
                sh '.venv/bin/pip --version'
            }
        }


        stage('Install Dependencies') {
                steps {
                    sh '.venv/bin/python -m pip install -r requirements.txt'
                    sh '.venv/bin/python -m pip check'
                }
            }

    }
}

