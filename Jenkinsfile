pipeline {
    agent any

    environment {
        IMAGE_NAME = 'python-app'
    }

    stages {
        stage('Clone Repo') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        
             stage('Build Docker Image') {
                steps {
                    sh 'docker build -t python-app .'
                    }
                }
            
            stage('Push to Docker Hub') {
                steps {
                    script {
                          sh '''
                docker rm -rf  hostel_container || true
                docker run -d --name hostel_container -p 8501:8501  python-app
                '''                       
                    }
                }
            }
        }
    }
}
