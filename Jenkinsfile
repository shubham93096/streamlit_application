pipeline {
    agent any

    parameters {
        string(
            name: 'DOCKER_IMAGE_NAME',
            defaultValue: 'vaibhavmungal/streamlit-app',
            description: 'Docker Hub repository name (e.g., username/repository)'
        )
    }

    environment {
        DOCKER_IMAGE = "${params.DOCKER_IMAGE_NAME}"
        IMAGE_TAG = "${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code from Git..."
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE}:${IMAGE_TAG} and latest..."
                script {
                    sh """
                        docker build \
                            -t ${DOCKER_IMAGE}:${IMAGE_TAG} \
                            -t ${DOCKER_IMAGE}:latest .
                    """
                }
            }
        }

        stage('Docker Hub Push') {
            steps {
                echo "Authenticating and pushing images to Docker Hub..."
                script {
                    withCredentials([usernamePassword(
                        credentialsId: "${env.DOCKER_CREDENTIALS_ID}",
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        sh """
                            echo "\$DOCKER_PASS" | docker login -u "\$DOCKER_USER" --password-stdin
                            docker push ${DOCKER_IMAGE}:${IMAGE_TAG}
                            docker push ${DOCKER_IMAGE}:latest
                            docker logout
                        """
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Cleaning up local Docker images..."
            sh """
                docker rmi ${DOCKER_IMAGE}:${IMAGE_TAG} ${DOCKER_IMAGE}:latest || true
            """
        }
        success {
            echo "Pipeline completed successfully! Docker image pushed to Docker Hub: ${DOCKER_IMAGE}:${IMAGE_TAG}"
        }
        failure {
            echo "Pipeline failed! Please check stage logs for details."
        }
    }
}
