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
                dir("${WORKSPACE}") {
                    sh '''
                        # Supprimer l'ancien venv s'il existe
                        rm -rf venv

                        # Créer un nouvel environnement virtuel
                        python3 -m venv venv

                        # Mettre à jour pip
                        ./venv/bin/python3 -m pip install --upgrade pip

                        # Installer les dépendances
                        ./venv/bin/pip install -r requirements.txt
                        #hmmm
                        # Lancer les tests (vérifie que le dossier app/tests existe)
                        ./venv/bin/python3 -m pytest app/tests --disable-warnings -q
                    '''
                }
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
                    # Arrêter et supprimer le conteneur existant
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
            echo "✅ Déploiement réussi ! L'application est en ligne sur http://localhost:5000"
        }
        failure {
            echo "❌ Le pipeline a échoué, vérifier les logs."
        }
        always {
            sh 'rm -rf venv || true'
        }
    }
}

