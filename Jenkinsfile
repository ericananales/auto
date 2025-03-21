pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/ericananales/auto.git'
            }
        }

        stage('Build') {
            steps {
                // If using Maven on Windows
                bat 'mvn clean package'  // Use 'bat' instead of 'sh'
            }
        }

        stage('Test') {
            steps {
                // If running tests on Windows
                bat 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Add Windows deployment scripts here
            }
        }
    }
}
