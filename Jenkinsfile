pipeline {
    agent any

    tools {
        maven 'Maven' // This must match the name in "Manage Jenkins > Tools"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/ericananales/auto.git'
            }
        }

        stage('Build') {
            steps {
                bat 'mvn clean package'  // Now uses the Jenkins-configured Maven
            }
        }

        stage('Test') {
            steps {
                bat 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }
}
