# Flask Hello Jenkins 🚀

Projet démontrant une intégration continue avec **Flask + Jenkins + Docker**.

## 📂 Structure
- `app/` : Code source Flask
- `Dockerfile` : Construction de l'image
- `Jenkinsfile` : Pipeline CI/CD
- `requirements.txt` : Dépendances
- `README.md` : Documentation

## ▶️ Lancer en local
```bash
docker build -t flask_hello_jenkins .
docker run -d -p 5000:5000 flask_hello_jenkins
