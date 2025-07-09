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

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                echo "Creating virtual environment..."
                python3 -m venv ${VENV_DIR}
                echo "Activating environment and installing dependencies..."
                #ls ${VENV_DIR}
                . ${VENV_DIR}/bin/activate
                #ls ./${VENV_DIR}/bin/pip
                #python3-pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                echo "Running tests..."
                #. ${VENV_DIR}/bin/activate && \
                #python3 -m unittest discover -s tests
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '#docker run -d -p 8081:8081 $IMAGE_NAME'
            }
        }
    }
}
