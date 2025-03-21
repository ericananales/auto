pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Ensure Jenkins clones the correct branch
                git branch: 'main', url: 'https://github.com/ericananales/auto.git'
            }
        }

        stage('Build') {
            steps {
                // Check if Maven is installed
                sh 'mvn -version'

                // Build the project (change if using npm, Gradle, etc.)
                sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                // Run tests
                sh 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Deployment scripts (e.g., SSH, Docker, Kubernetes, etc.)
            }
        }
    }
}
