pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Cloning the repository from the provided URL
                git 'https://github.com/ericananales/auto.git'
            }
        }

        stage('Build') {
            steps {
                // Building the project, replace with your appropriate build command
                sh 'mvn clean package'  // Replace with 'npm install' or 'python setup.py' if needed
            }
        }

        stage('Test') {
            steps {
                // Running tests, replace with your appropriate test command
                sh 'mvn test'  // Replace with the appropriate test command for your project
            }
        }

        stage('Deploy') {
            steps {
                // Deployment logic
                echo 'Deploying application...'
                // Add deployment scripts here (e.g., kubectl, SSH, etc.)
            }
        }
    }
}
