# Execute o comando docker abaixo para iniciar o container com o MongoDB.
# docker run --name mongo-container-2 vsgroot/rent-right-db


import pymongo
import docker

class MongoDBManager:
    _client = None
    _db = None
    _collection = None

    @staticmethod
    def _get_mongo_client():
        if MongoDBManager._client is None:
            client = docker.from_env()
            container = client.containers.get('mongo-container-2')
            container_info = container.attrs
            networks = container_info['NetworkSettings']['Networks']
            network_info = networks[list(networks.keys())[0]]  # Assuming only one network is used
            container_ip = network_info['IPAddress']
            MongoDBManager._client = pymongo.MongoClient(host=container_ip, port=27017,
                                                        username='root', password='example',
                                                        authSource='admin')
        return MongoDBManager._client

    @staticmethod
    def _get_database():
        if MongoDBManager._db is None:
            client = MongoDBManager._get_mongo_client()
            MongoDBManager._db = client['rent-right']
        return MongoDBManager._db

    @staticmethod
    def _get_collection():
        if MongoDBManager._collection is None:
            db = MongoDBManager._get_database()
            MongoDBManager._collection = db['rentRight']
        return MongoDBManager._collection

    @staticmethod
    def insert_document(document):
        collection = MongoDBManager._get_collection()
        result = collection.insert_one(document)
        print("Document inserted with ID:", result.inserted_id)

    @staticmethod
    def update_document(query, update):
        collection = MongoDBManager._get_collection()
        result = collection.update_one(query, update)
        print("Document updated:", result.modified_count)

    @staticmethod
    def delete_document(query):
        collection = MongoDBManager._get_collection()
        result = collection.delete_one(query)
        print("Document deleted:", result.deleted_count)

    @staticmethod
    def display_documents():
        collection = MongoDBManager._get_collection()
        documents = collection.find()
        for document in documents:
            print(document)


# Inserindo um documento
#MongoDBManager.insert_document({'region':'Camaragibe', 'price': 1500, 'houseType': 'apartment', 'sqFeet': 1200, 'beds': 3, 'baths': 1, 'catsAllowed':1, 'dogsAllowed':1, 'smokingAllowed':1, 'comesFurnished':1, 'latitude':81.4245, 'longitude': -23.4421,'state':'ca'})

# Atualizando um documento
#MongoDBManager.update_document({"region": "Camaragibe"}, {"$set": {"region": "Paulista"}})

# Excluindo um documento
#MongoDBManager.delete_document({"key": "new_value"})
         
# Mostrando documentos
#MongoDBManager.display_documents()
