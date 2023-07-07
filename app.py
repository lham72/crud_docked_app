# import de mes librairies

from flask import Flask, jsonify, request
from pymongo import MongoClient
import os
from bson.objectid import ObjectId


# creation de mon application flask
app = Flask(__name__)

# information de connexion à la base de données
host = os.environ.get("MONGO_HOST", "localhost")
port = 27017

# creation du client de connexion
client = MongoClient(host=host, port=port)

# recuperation de ma base de données
mabdd = client.demo


# recuperation de ma collection
col = mabdd.users

# premiere route sur "/"
@app.route("/")
def hello_world():
    informations = {
    "Hello": "World!",
    "mabdd_type" :str(type(mabdd)),
    "mabdd" : str(mabdd)
    }

    return jsonify({"BDD":informations})


# test flask 123
@app.route("/test123/<msg>", methods=["GET"])
def test123(msg):
    return f'bonjour {msg}'


# methode read all
@app.route("/users", methods=["GET"])
def get_users():
    datas = list(col.find())
    for data in datas:
        data["_id"] = str(data["_id"])
    return jsonify({"users": datas})


# methode find by id
@app.route("/users/<id>", methods=["GET"])
def get_user(id):
    data = col.find_one({'_id': ObjectId(id)})
    data["_id"] = str(data["_id"])
    return jsonify({"user": data})


# methode pour creer un user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    result = col.insert_one(data)
    data["_id"] = str(result.inserted_id)
    return jsonify({"new_user": data})


# methode pour mettre à jour un user
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    data["_id"] = ObjectId(id)
    result = col.replace_one({'_id': ObjectId(id)}, data)
    data["_id"] = str(result.upserted_id)
    return jsonify({"update_user": data})


# methode pour supprimer un user
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    data_delete = col.find_one({'_id': ObjectId(id)})
    data_delete["_id"] = str(data_delete["_id"])
    col.delete_one({'_id': ObjectId(id)})
    return jsonify({"delete_user": data_delete})


# lancement de mon application
if __name__ == "__main__":
    app.run(host="0.0.0.0",port=9001, debug=True)