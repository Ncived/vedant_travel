pipeline {
    agent any
    environment {
        // SonarCloud environment variables
        SONAR_HOST_URL = 'https://sonarcloud.io'
        SONAR_PROJECT_KEY = 'vedant_travel'
        SONAR_ORGANIZATION = 'ncived'
        SONAR_TOKEN = credentials('sonarcloud-token') // Add the token in Jenkins credentials
        scannerHome = tool 'sonarcloud-scanner'
    }


    stages {
        stage('checkout') {
            steps {
                git credentialsId: 'test', url: 'https://github.com/Ncived/vedant_travel.git'
            }
        }
        stage('Set Up Environment') {
            steps {
                sh '''#!/bin/bash
                    python3 -m venv myenv
                    source myenv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pip install pylint
                '''
            }
        }
        stage('Run Static Analysis with Pylint') {
            steps {
                sh '''#!/bin/bash
                    python3 -m venv myenv
                    source myenv/bin/activate
                    pylint $WORKSPACE/*.py || true
                    pylint $WORKSPACE/travel_planner/*.py || true
                    pylint $WORKSPACE/trips/*.py || exit 0
                '''
            }
        }
        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv(installationName: 'sonarcloud') {
                        sh '''
                            ${scannerHome}/bin/sonar-scanner \
                               -Dsonar.projectKey=$SONAR_PROJECT_KEY \
                               -Dsonar.organization=$SONAR_ORGANIZATION \
                               -Dsonar.host.url=$SONAR_HOST_URL \
                               -Dsonar.login=$SONAR_TOKEN
                        '''
                    }
                }
            }
        }
       stage('Deploy to EC2') {
    steps {
        script {
            sh '''
                # Build the Docker image
                docker build --no-cache -t travel-app .
                
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
