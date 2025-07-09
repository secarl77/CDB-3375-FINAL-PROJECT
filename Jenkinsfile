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
                sh ''''
                echo "Installing systems dependecies..."
                sudo apt-get update
                sudo apt-get install -y python3.11 python3.11-venv python3.11-dev python3-pip
                echo 'Creating virtual environment...'
                python3.11 -m venv ${VENV_DIR}
                echo "Enable virtual environment..."
                source ${VENV_DIR}/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                ''''
            }
        }

        stage('Test') {
            steps {
                echo 'executing tests...'
		        sh 'python3 -m unittest discover -s tests'
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

