# Étape 1 : Builder l’image
FROM python:3.11-slim as builder

WORKDIR /app

# Installer dépendances système
RUN apt-get update && apt-get install -y build-essential

# Copier requirements et installer
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Étape 2 : Image finale
FROM python:3.11-slim

WORKDIR /app

# Copier depuis builder
COPY --from=builder /root/.local /root/.local
COPY app ./app

# Variables d'environnement
ENV PATH=/root/.local/bin:$PATH

EXPOSE 5000

# Démarrage avec gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app.app:app"]
