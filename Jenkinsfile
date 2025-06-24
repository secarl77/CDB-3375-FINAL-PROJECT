pipeline {
    agent any

    enviroment {
        IMAGE_NAME = "cdb-3375-final-project"
    }

    stages {
        stage('Checkout') {
            steps {
        	checkout scm
	     }
    }
        stage('Build') {
            steps {
                echo 'building the application...'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Test') {
            steps {
                echo 'executing tests...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment the application...'
                docker run -d -p 8081:8081 $IMAGE_NAME
            }
        }
    }
}

