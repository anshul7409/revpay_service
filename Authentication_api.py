from argon2 import PasswordHasher
from DB_conn import revpayDB
from Session import SessionManager
from flask import jsonify
ph = PasswordHasher()

class Authentication:
    def __init__(self,username,password):
        self.__username = username
        self.__password = password
        DB = revpayDB()
        self.__session = SessionManager()
        self.__users_collection = DB.get_collection('users_collection')
        self.__user = self.__users_collection.find_one({'username':username})
    
    def register(self):
        if self.__session.isactive():
           self.__session.delete_session()
        hashed_password = ph.hash(self.__password)
        if self.__users_collection.find_one({'username': self.__username}):
            return jsonify({'message': 'User already exists!'}), 400
        user_data = {'username': self.__username, 'password': hashed_password}
        self.__users_collection.insert_one(user_data)
        return jsonify({'message': 'User registered successfully!'})
    
    def login(self):
        if self.__session.isactive():
            return jsonify({'message': 'user already logged in'})
        else:
            try:
                if ph.verify(self.__user['password'], self.__password):
                    print(self.__user)
                    self.__session.activate_session([self.__user['username'],str(self.__user['_id'])])
                    return jsonify({'message': 'Login successful!'})
            except:
                return jsonify({'message': 'Invalid password'}), 401
        return jsonify({'message': 'Invalid email or password'}), 401