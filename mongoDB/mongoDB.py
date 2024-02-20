# Execute o comando docker abaixo para iniciar o container com o MongoDB.
# docker run --name mongo-container-2 vsgroot/rent-right-db


import logging
from pymongo import MongoClient
from bson import ObjectId
from typing import Any, Dict, List, Optional
import re

class MongoDBManager:

    # Configure the logger
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    _client: MongoClient = MongoClient("mongodb://root:example@localhost:27017/rent-right?authSource=admin")
    _db = _client.rent_right
    _collection = _db.rentRight

    @staticmethod
    def _get_database():
        return MongoDBManager._db

    @staticmethod
    def _get_collection():
        if MongoDBManager._collection is None:
            db = MongoDBManager._get_database()
            MongoDBManager._collection = db['rentRight']
        return MongoDBManager._collection
    
    @staticmethod
    def insert_data(data: Dict[str, Any]) -> Optional[Any]:
        """
        Insert data into a collection.
        """
        try:
            status = MongoDBManager._get_collection().insert_one(data)
            MongoDBManager.logger.info(f'Data inserted successfully. ID: {status.inserted_id}')
            return status.inserted_id
        except Exception as e:
            MongoDBManager.logger.error(f'Error inserting data: {str(e)}')
            raise

    @staticmethod
    def read_data(property_id: Optional[int] = None) -> List[Dict[str, Any]]:
        """
        Read documents in the collection based on a filter (property_id).
        """
        try:
            filter_query = {} if property_id is None else {'_id': property_id}
            data = MongoDBManager._get_collection().find(filter_query)
            
            # Convertendo o objeto ObjectId do MongoDB para uma string para facilitar o uso
            result = [{'id': str(document['_id']), **document} for document in data]
            
            MongoDBManager.logger.info(f'Reading successful. Total documents: {len(result)}')
            return result
        except Exception as e:
            MongoDBManager.logger.error(f'Error reading data: {str(e)}')
            raise


    @staticmethod
    def update_data(filter_query: Dict[str, Any], update_query: Dict[str, Any]) -> int:
        print('oi')
        """
        Update documents in the collection based on a filter.
        """
        try:
            status = MongoDBManager._get_collection().update_many(filter_query, update_query)
            MongoDBManager.logger.info(f'Update successful. Modified documents: {status.modified_count}')
            return status.modified_count
        except Exception as e:
            MongoDBManager.logger.error(f'Error updating data: {str(e)}')
            raise

    @staticmethod
    def delete_data(filter_query: Dict[str, Any]) -> int:
        """
        Delete documents in the collection based on a filter.
        """
        try:
            status = MongoDBManager._get_collection().delete_many(filter_query)
            MongoDBManager.logger.info(f'Deletion successful. Deleted documents: {status.deleted_count}')
            return status.deleted_count
        except Exception as e:
            MongoDBManager.logger.error(f'Error deleting data: {str(e)}')
            raise

    @staticmethod
    def display_documents():
        collection = MongoDBManager._collection
        documents = collection.find()
        
        return documents
    
    @staticmethod
    def get_document_by_id(collection, document_id):
        # Converta a string do ID para o formato ObjectId
        object_id = document_id

        # Use find_one para obter o documento pelo ID
        document = collection.find_one({"_id": object_id})

        print(document)
        return document
    
    @staticmethod
    def get_documents_with_conditions(conditions):
        try:
            filter_query = {}

            for condition in conditions:
                # Split condition into field, operator, and value
                split_condition = re.split(r'\s+|(?<!\d)([=<>]+)(?!=)', condition)
                field, operator, value = split_condition[0], split_condition[1], split_condition[2]

                # Convert value to the appropriate type (int, float, or string)
                if field not in ['region_name', 'description']:
                    value = int(value) if value.isdigit() else float(value)

                # Handle LIKE operator for string fields
                if operator.upper() == 'LIKE':
                    filter_query[field] = {'$regex': value, '$options': 'i'}
                else:
                    filter_query[field] = {f'${operator}': value}

            documents = MongoDBManager._get_collection().find(filter_query)
            result = list(documents)

            MongoDBManager.logger.info(f'Retrieved documents based on conditions. Total documents: {len(result)}')
            return result

        except Exception as e:
            MongoDBManager.logger.error(f'Error retrieving data with conditions: {str(e)}')
            raise





"""      
banco = MongoDBManager()
#banco.get_document_by_id(banco._collection ,"65d41776e4dde60daf295d56")
string_id = "65d41668e4dde60daf295d43"

# Converta a string para ObjectId
object_id = ObjectId(string_id)
banco.get_document_by_id(banco._collection, object_id)
lista = list(banco.display_documents())
print(len(lista))


# Exemplo de uso:
banco = MongoDBManager()
# Inserir dados
sensor_data = {"id": 1, "e": 25, "humidity": 50}
inserted_id = banco.insert_data(sensor_data)
print("Documento inserido com ID:", inserted_id)

# Ler dados
data = banco.read_data()
print("Dados na coleção:")
for document in data:
    print(document)

# Atualizar dados
filter_query = {"id": 1}
update_query = {"$set": {"humidity": 60}}
modified_count = banco.update_data(filter_query, update_query)
print("Número de documentos atualizados:", modified_count)

# Deletar dados
filter_query = {"id": 1}
deleted_count = banco.delete_data(filter_query)
print("Número de documentos deletados:", deleted_count)

# Inserindo um documento
#MongoDBManager.insert_document({'region':'Camaragibe', 'price': 1500, 'houseType': 'apartment', 'sqFeet': 1200, 'beds': 3, 'baths': 1, 'catsAllowed':1, 'dogsAllowed':1, 'smokingAllowed':1, 'comesFurnished':1, 'latitude':81.4245, 'longitude': -23.4421,'state':'ca'})

# Atualizando um documento
#MongoDBManager.update_document({"region": "Camaragibe"}, {"$set": {"region": "Paulista"}})

# Excluindo um documento
#MongoDBManager.delete_document({"key": "new_value"})
         
# Mostrando documentos
MongoDBManager.display_documents()
"""