# Image Python utilisée par l'application
FROM python:3.14-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier la liste des dépendances
COPY requirements.txt .

# Installer Flask et PyMySQL
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app.py .

# Documenter le port utilisé par Flask
EXPOSE 5000

# Lancer l'application au démarrage du conteneur
CMD ["python", "app.py"]

# Ansible demandera plus tard à Docker de construire une image à partir de ce fichier.
# et Flask ecoutera sur le port 5000
