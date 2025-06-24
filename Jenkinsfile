pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
        	checkout scm
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

