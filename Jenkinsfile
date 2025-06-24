pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
		git credentialsId: '8a2b59a0-bcd4-497e-bdb3-b7489e053370', url: 'https://github.com/secarl77/CDB-3375-FINAL-PROJECT.git'}
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

