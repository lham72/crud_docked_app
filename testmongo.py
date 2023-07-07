"""
Exemple de communication avec une base mongo db
Lexique:
* Base de données <=> database
* table <=> collection
* row <=> document
"""
# importation des bibliothèques
from pymongo import MongoClient

# info de ma base de données
host = "localhost"
port = 27017

# connexion à la base de données

client = MongoClient(host=host, port=port)

#récupération de ma base de données
mabdd = client.demo


print("ma bdd : \n", type(mabdd))
print("ma bdd : \n", mabdd)

#récupération de ma collection
ma_collection = mabdd.users

print("ma collection : \n", type(ma_collection))
print("ma collection : \n", ma_collection)

# Ajout datas dans BDD au format JSON
new_user = {
    "name": "John",
    "age": 30,
    "address": "New York"
    }
# insertion du document
reponse_new_id = ma_collection.insert_one(new_user)
# recuperation de l'id à partir de l'objectID
new_id = str(reponse_new_id.inserted_id)
#attributuin de son id à ma nouvel data enregistrée
new_user["_id"] = new_id
print("new user : \n", new_user)

# recuperation de tous les users de ma collection
mes_users = ma_collection.find()
print("mes users : \n", list(mes_users))