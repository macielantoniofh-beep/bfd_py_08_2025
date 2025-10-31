'''diferença banco sql e nosql - mais simples e menos burocratico
estrutura

relacionamento entre as coleções (tabela) - os campos são documentos
firebase - olhar
json file - arquivo - chaves como dicionarios

import pymongo
cliente1 = pymongo.MongoClient("mongodb://localhost:27017/")

cliente = pymongo.MongoClient("mongodb+srv://macielantoniofh_db_user:7ST9rHW0at7kKzuf@fh.qbdsv9c.mongodb.net/?appName=Fh")

lojinha = cliente ["lojinhadb"]
users = lojinha ["users"]
doc = ['nome": "Antonio", "idade": 30, "Trabalho":"Analista"]
print(users.find_one({"nome":{"$gt":"Fre"}}))
users.delete_one({"nome":"Antonio"})
print(users.find_one({"nome":{$gt:"Fre}}))
print(cliente.list_database_names())
print(cliente)

instalar mongodb
ou acessar pelo atlas

'''
import pymongo

cliente = pymongo.MongoClient("mongodb+srv://macielantoniofh_db_user:7ST9rHW0at7kKzuf@fh.qbdsv9c.mongodb.net/?appName=Fh")
print(cliente)
