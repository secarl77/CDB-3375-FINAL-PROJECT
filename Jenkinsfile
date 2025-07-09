pipeline {
    agent any

    environment {
        IMAGE_NAME = "cdb-3375-final-project"
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
        	checkout scm
	     }
    }
        stage('Install Dependencies') {
            steps {
                sh '''
                #!/bin/bash
                echo 'Creating virtual environment...'
                python3.11 -m venv ${VENV_DIR}
                echo 'Enable virtual environment and install dependencies...'
                source ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
    }


        stage('Test') {
            steps {
                sh '''
                echo "Executing unitary tests..."
                source ${VENV_DIR}/bin/activate
                python -m unittest discover -s tests
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'building the application...'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }



        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh 'docker run -d -p 8081:8081 $IMAGE_NAME'
            }
        }
    }
}

