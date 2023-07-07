# image source
FROM python:3 

# récup dependances du projet
COPY requirements.txt ./

# installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Ajout de mon application Flask
COPY app.py app.py

# Ouvrir le port qui m'iteresse
EXPOSE 9001

# demarrer mon application
CMD [ "python", "app.py" ]