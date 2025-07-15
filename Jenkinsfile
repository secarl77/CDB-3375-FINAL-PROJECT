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
                #!/bin/bash
                echo "Cleaning virtual environment..."
                rm -rfv venv

                echo "Creating virtual environment"
                python3.11 -m venv ${VENV_DIR}

                echo "Activating environment and installing dependencies..."
                . ${VENV_DIR}/bin/activate
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flak App in Background'){
            steps {
                sh '''
                #!/bin/bash
                echo "starting Flask application..."
                . ${VENV_DIR}/bin/activate && \
                nohup ./venv/bin/python3 run.py > flask.log 2>&1 &

                echo "Waiting for Flask..."
                for i in {1..10}; do
                    curl -s http://localhost:8081/login && break
                    echo "⏳ Esperando..."
                    sleep 2
                done
                echo "[🧪] Ejecutando pruebas UI con Selenium..."
                ./venv/bin/python -m unittest discover -s tests -p "test_ui_*.py"
                '''
            }

        }
        stage('Run Tests') {
            steps {
                sh '''
                echo "Running tests..."
                . ${VENV_DIR}/bin/activate && \
                python3.11 -m unittest tests/test_app.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'docker run -d -p 8081:8081 $IMAGE_NAME'
            }
        }
    }
}
