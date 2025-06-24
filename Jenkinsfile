pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/secarl77/CDB-3375-FINAL-PROJECT'
            }
        }

        stage('Build') {
            steps {
                echo 'Construyendo la aplicación...'
            }
        }

        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Desplegando aplicación...'
            }
        }
    }
}

