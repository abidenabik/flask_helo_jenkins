git clone https://github.com/abidenabik/flask_helo_jenkins.git
cd flask_helo_jenkins

# Virtual env
python3 -m venv venv
./venv/bin/pip install --upgrade pip
./venv/bin/pip install -r requirements.txt

# Build Docker
docker build -t flask_hello_jenkins:latest .

# Stop & remove ancien conteneur
docker stop flask_hello_jenkins || true
docker rm flask_hello_jenkins || true

# Run conteneur
docker run -d --name flask_hello_jenkins -p 5000:5000 flask_hello_jenkins:latest
