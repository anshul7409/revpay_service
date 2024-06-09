from flask import session
class SessionManager:
    def __init__(self):
        self.__session = session

    def activate_session(self,name):
        self.__session['user'] = name 

    def isactive(self):
        return self.__session.get('user',None) is not None 
    
    def delete_session(self):
        self.__session.pop('user', None)
    
    def get_session(self):
        return self.__session.get('user',None)