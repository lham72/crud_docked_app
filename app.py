from flask import Flask, request, jsonify
from pymongo import MongoClient
import os


app = Flask(__name__)

# mongo db host
host = os.environ.get('MONGO_HOST', "localhost")
port = 27017

# connexion à la base de données
client = MongoClient(host=host, port=port)

#récupération de ma base de données
mabdd = client.demo


# route test
@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World! \n' + str(type(mabdd)) + '\n mabdd : \n' + str(mabdd)

# affiche tous les users
@app.route('/users', methods=['GET'])
def get_users():
    return 'Tous les users'

# find by id
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    return f'Le user qui a l\'id : {id}'

# create user
@app.route('/users/<id>', methods=['POST'])
def create_user(id):
    return None

# maj user
@app.route('/users', methods=['PUT'])
def update_user():
    return None

# suppr user
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    return None



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9001, debug=True)