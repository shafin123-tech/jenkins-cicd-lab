
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
    }
}
  