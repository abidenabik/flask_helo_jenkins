pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "flask_hello_jenkins"
        DOCKER_TAG = "latest"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', credentialsId: 'gith-pat', url: 'https://github.com/abidenabik/flask_helo_jenkins.git'
            }
        }
        stage('Install Dependencies & Test') {
            steps {
                sh '''
                    # Supprimer l'ancien venv s'il existe
                    rm -rf venv
                    
                    # Créer un nouvel environnement virtuel
                    python3 -m venv venv
                    
                    # Vérifier que le venv est bien créé
                    ls -la venv/bin/
                    
                    # Utiliser explicitement le pip du venv (chemin absolu)
                    /var/lib/jenkins/workspace/flask_hello_jenkins_pipeline/venv/bin/python -m pip install --upgrade pip
                    /var/lib/jenkins/workspace/flask_hello_jenkins_pipeline/venv/bin/pip install -r requirements.txt
                    
                    # Exécuter les tests avec le python du venv
                    /var/lib/jenkins/workspace/flask_hello_jenkins_pipeline/venv/bin/python -m pytest app/tests --disable-warnings -q
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
                    # Arrêter et supprimer le conteneur existant s'il existe
                    docker ps -q --filter "name=flask_hello_jenkins" | xargs -r docker stop
                    docker ps -aq --filter "name=flask_hello_jenkins" | xargs -r docker rm
                    
                    # Démarrer le nouveau conteneur
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
        always {
            // Nettoyer l'environnement virtuel
            sh 'rm -rf venv || true'
        }
    }
}