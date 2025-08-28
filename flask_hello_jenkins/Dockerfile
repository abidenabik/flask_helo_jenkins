FROM python:3.11-slim

WORKDIR /app

# Installer dépendances système
RUN apt-get update && apt-get install -y build-essential

# Copier requirements et installer directement
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app ./app

EXPOSE 5000

# Démarrage avec gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app.app:app"]
