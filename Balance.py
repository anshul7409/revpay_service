from Session import SessionManager
from DB_conn import revpayDB
from flask import jsonify
class BalanceManager:
    def __init__(self,account_no):
        self.__session_ins = SessionManager()
        __session = self.__session_ins.get_session()
        self.__revpayid = __session[1]
        self.__account_no = account_no
        DB_ins = revpayDB()
        self.__accounts_collection = DB_ins.get_collection('users_account')

    def check_balance(self):
        if self.__session_ins.isactive():
            accounts = self.__accounts_collection.find_one({'user_id': self.__revpayid})
            if accounts:
                account = next((acc for acc in accounts['accounts'] if acc['account_number'] == self.__account_no), None)
                if account:
                    balance = account['balance']
                    return jsonify({"current balance": balance})
                else:
                    return jsonify({"message" : "Account doesnt't exists!"})
            else:
                return jsonify({"message": "Invalid Account number!"}), 404
        return jsonify({"message": "Please login to check balance"})
