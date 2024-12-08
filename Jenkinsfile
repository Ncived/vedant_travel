pipeline {
    agent any

    stages {
        stage('checkout') {
            steps {
                git credentialsId: 'githubvedant', url: 'https://github.com/Ncived/vedant_travel.git'
            }
        }
       stage('Deploy to EC2') {
    steps {
        script {
            sh '''
                # Build the Docker image
                docker build --no-cache -t travel-app.
                
                # Stop any existing container and run the new image
                docker stop travel-app || true
                docker rm travel-app || true
                
                docker volume rm django-db-volume || true
                docker volume create django-db-volume

                docker run -d -p 8000:8000 --name travel-app \
                -v django-db-volume:/app \
                travel-app

            '''
        }
            }
        }
    }
}
