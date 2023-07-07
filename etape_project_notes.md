# Application dockerisé

## add files
app.py
Dockerfile
docker-compose.yml

## init
py -m venv venv
demarrarer l'environment
.\venv\Script\activate
pip install flask
pip freeze > requirements.txt

## Start dev app
Flask app helloWord!

```python
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'
```

### Add routes
- **affiche tous les users**
```python
@app.route('/users', methods=['GET'])
```
- **find by id**
```python
@app.route('/users/<id>', methods=['GET'])
```
- **create user**
```python
@app.route('/users/<id>', methods=['POST'])
```
- **maj user**
```python
@app.route('/users', methods=['PUT'])
```
- **suppr user**
```python
@app.route('/users/<id>', methods=['DELETE'])
```

### Constituer le Dockerfile
- image source, "FROM python"
- récup dependances du projet, "COPY requirements.txt ./"
- installer les dépendances, "RUN pip install --no-cache-dir -r requirements.txt"
- Ajout de mon application Flask, "COPY app.py app.py"
- demarrer mon application, "CMD [ "python", "app.py" ]"
- **Run build : "docker build -t crud_pyapp ."**

### Test de l'app
```bash
docker run -dit --name testcrudapp -p 9001:9001 crud_pyapp
```

### Intégration de mongodb et de son ui mongo-express
- **utilisation d'un docker-compose mongodb comme base**
[Here](https://hub.docker.com/_/mongo)
```yaml
# liste des différents conteneurs
services:
  # conteneur pour mongodb
  mongo:
    # image mongo
    image: mongo
    container_name: mongodb
    restart: always
    # ouverture du port mongo
    ports:
      - 27017:27017
    # volume pour persister mes données
    volumes:
      - "./data/db:/data/db"
    # deploiement dans un réseau
    networks:
      - app-mongo-VNet

  # conteneur de mon conteneur
  mongo-express:
    # image de mon conteneur
    image: mongo-express
    restart: always
    # ouverture du port de l'ui
    ports:
      - 8081:8081
    environment:
      # Nom du service de la BDD
      ME_CONFIG_MONGODB_SERVER: mongodb
    depends_on:
      - mongodb
    networks:
      - app-mongo-VNet

# fabrication du réseau app-mongo-VNet parrallèle au réseau bridge par défaut
networks:
  app-mong-VNet:
    driver: bridge

```
### Ajout de l'appli python
```yaml
  # conteneur de mon application flask
  crudapp:
    #construire à la volée mon image
    build: .
    # ouverture des ports du conteneur de l'app python
    ports:
      - 9002:9001
    networks:
      - app-mongo-VNet
    depends_on:
      - mongodb
```
### Continuation du dev, ajout du CRUD avec mongodb
- fichier test : testmongo.py
- solution pour réferencer la BDD mongo
    - **Côté docker-compose:** Au niveau du service app python
        * ```yaml
            # ajout d'une variable pour récupérer l'ip du conteneur mongodb
            # en fesant réference au nom du **SERVICE**
            environment:
            - MONGO_HOST=mongodb
        ```
    - **Côté de l'appli python:**
        * ```bash
            import os

            # mongo db host
            host = os.environ.get('MONGO_HOST', "localhost")
 
 
       ```
- Dev interfaçage mongdb
    - 
