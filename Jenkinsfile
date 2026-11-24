
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
    }
}
