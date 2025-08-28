pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "flask_hello_jenkins"
        DOCKER_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'gith-pat', url: 'https://github.com/abidenabik/flask_hello_jenkins.git'
            }
        }

        stage('Install Dependencies & Test') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pytest app/tests --disable-warnings -q
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh '''
                docker ps -q --filter "name=flask_hello_jenkins" | xargs -r docker stop
                docker ps -aq --filter "name=flask_hello_jenkins" | xargs -r docker rm
                docker run -d --name flask_hello_jenkins -p 5000:5000 $DOCKER_IMAGE:$DOCKER_TAG
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Déploiement réussi ! L'application est en ligne sur http://<IP_SERVEUR>:5000"
        }
        failure {
            echo "❌ Le pipeline a échoué, vérifier les logs."
        }
    }
}
