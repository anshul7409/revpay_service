from urllib.parse import quote_plus
from pymongo import MongoClient
from Schema import Schema
import os
db_username = os.getenv('DBNAME')
db_password = os.getenv('PASSWORD')
class revpayDB:
    def __init__(self):
        self.__DATABASE_URI = "mongodb+srv://{}:{}@cluster0.dqwgi9f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(quote_plus(db_username), quote_plus(db_password))
        self.__client =  MongoClient(self.__DATABASE_URI)
        self.__db =  self.__client['users_database']
    
    def get_conn(self):
        return self.__client
    
    def get_db(self):
        return self.__db 
    
    def get_collection(self,collection):
        schema_obj = Schema(collection)
        schema = schema_obj.get_schema()
        try:
          self.__db.create_collection(collection, validator={"$jsonSchema": schema})
        except:
          print("collection already exisits")
        return self.__db[collection]