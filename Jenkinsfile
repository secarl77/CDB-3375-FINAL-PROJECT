pipeline {
    agent any

    environment {
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
		sh 'python3 -m unittest discover -s tests'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deployment the application...'
                sh 'docker run -d -p 8081:8081 $IMAGE_NAME'
            }
        }
    }
}

