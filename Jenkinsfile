pipeline {
    agent { label 'jenkins' }
    environment {
        IMAGE_NAME = "cdb-3375-final-project"
        VENV_DIR = "${WORKSPACE}/venv"
        IMAGE_TAG = "v1"
    }

    stages {
        stage('Checkout') {
            steps {
                sh 'whoami'
                sh 'hostname'
                sh 'echo $VENV_DIR'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                #!/bin/bash
                echo "Cleaning virtual environment..."
                rm -rfv venv

                echo "Creating virtual environment"
                python3 -m venv ${VENV_DIR}

                echo "Activating environment and installing dependencies..."
                . ${VENV_DIR}/bin/activate
                ./venv/bin/pip install --upgrade pip
                ./venv/bin/pip install -r requirements.txt
                '''
            }
        }

        stage('Run Flak App in Background and making UI tests'){
            steps {
                sh '''
                #!/bin/bash
                echo "starting Flask application..."
                . ${VENV_DIR}/bin/activate && \
                nohup ./venv/bin/python3 run.py > flask.log 2>&1 &
                FLASK_PID=$!
                echo "✅ Flask started with PID: $FLASK_PID"

                echo "Waiting for Flask..."
                for i in {1..10}; do
                    curl -s http://localhost:8081/login && break
                    echo "⏳ Waiting..."
                    sleep 2
                done
                echo "[🧪] Executing UI test with Selenium..."
                ./venv/bin/python -m unittest discover -s tests -p "test_ui_*.py"
                echo "🛑 Stopping Flask application (PID: $FLASK_PID)..."
                kill $FLASK_PID
                '''
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credential', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    // Login to DockerHub and push image
                    sh '''
                    docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
                    docker tag $IMAGE_NAME:$IMAGE_TAG $DOCKER_USERNAME/$IMAGE_NAME:$IMAGE_TAG
                    docker push $DOCKER_USERNAME/$IMAGE_NAME:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy') {
            agent { label 'webapp' }
            steps {
                echo 'Deploying application...'
                withCredentials([sshUserPrivateKey(credentialsId: 'ec2-ssh-key', keyFileVariable: 'KEY')]) {
                    sh '''
                        echo "🚀 Haciendo deploy en remoto vía SSH..."

                        ssh -i "$KEY" -o StrictHostKeyChecking=no ubuntu@35.182.245.204 '
                            docker stop flask_app || true
                            docker rm flask_app || true
                            docker pull $DOCKER_IMAGE
                            docker run -d --name flask_app -p 8081:8081 $DOCKER_IMAGE
                        '
                    '''
                }
            }
        }
    }
}
