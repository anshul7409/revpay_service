from urllib.parse import quote_plus
from pymongo import MongoClient
import os
db_username = os.getenv('DBNAME')
db_password = os.getenv('PASSWORD')
db_username_bytes = db_username.encode('utf-8')
db_password_bytes = db_password.encode('utf-8')
class revpayDB:
    def __init__(self):
        self.__DATABASE_URI = "mongodb+srv://{}:{}@cluster0.dqwgi9f.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0".format(quote_plus(db_username_bytes), quote_plus(db_password_bytes))
        self.__client =  MongoClient(self.__DATABASE_URI)
        self.__db =  self.__client['users_database']
    
    def get_conn(self):
        return self.__client
    
    def get_db(self):
        return self.__db 
    
    def get_collection(self,collection):
        collection = self.__db[collection]
        return collection