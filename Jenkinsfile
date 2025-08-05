pipeline {
    agent any
    environment {
        IMAGE_NAME = "cdb-3375-final-project"
        VENV_DIR = "venv"
        IMAGE_TAG = "v1"
    }

    stages {
        stage('Checkout') {
            steps {
                sh 'whoami'
                sh 'hostname'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'sudo docker build -t $IMAGE_NAME:$IMAGE_TAG .'
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

        stage('Start Flask App on Jenkins') {
            steps {
                sh '''
                    #!/bin/bash
                    echo "🚀 Iniciando la aplicación Flask en background..."

                    # Activa entorno virtual y lanza la app
                    . ${VENV_DIR}/bin/activate && \
                    ./venv/bin/python3 run.py

                    # Guarda el PID para luego poder detenerla
                    echo $! > flask.pid
                    echo "✅ Flask iniciado en background (PID guardado)"
                '''
            }
        }
    /*     stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credential', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
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
            steps {
                echo 'Deploying application...'
                sshagent(['ec2-ssh-key']) {
                sh """
                ssh -o StrictHostKeyChecking=no ubuntu@15.222.248.38 '
                    docker stop webapp || true
                    docker rm webapp || true
                    docker pull secarl/${IMAGE_NAME}:${IMAGE_TAG}
                    docker run -d --name webapp -p 8081:8081 secarl/${IMAGE_NAME}:${IMAGE_TAG}
                    '
                """
                }
            }
        }*/
    }
}
