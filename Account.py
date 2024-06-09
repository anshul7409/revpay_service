from flask import jsonify
import uuid
from DB_conn import revpayDB
from Session import SessionManager

class AccountManager:
    def __init__(self,account_number,ifsc_code):
        self.__account_number = account_number
        self.__ifsc_code = ifsc_code
        self.__db = revpayDB()
        self.__session = SessionManager()
        self.__active = 1
        users_collection = self.__db.get_collection('users_collection')
        username = self.__session.get_session() 
        self.__user = users_collection.find_one({'username':username})
        self.__users_account = self.__db.get_collection('users_account')
    
    def inactive(self):
        self.__active = 0

    def createaccount(self):
        if self.__session.isactive():     
            id = self.__user['_id']
            uid = str(uuid.uuid4())
            account_data = {"UID":uid, "account_number": self.__account_number, "ifsc_code": self.__ifsc_code, "balance":0.0, "active":self.__active}
            self.__users_account.update_one(
                {'user_id': id},
                {'$push': {'accounts': account_data}},
                upsert=True
            )
            return jsonify({'message': 'Account Created successfully'}),200
        return jsonify({'message': 'Please Login to create account!'}),401
    