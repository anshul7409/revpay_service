from DB_conn import revpayDB
from flask import jsonify
from Session import SessionManager

class TransactionManager:
    def __init__(self,amount,account_no):
        self.__session_ins = SessionManager()
        self.__session = self.__session_ins.get_session()
        self.__id = self.__session[1]
        self.__account_no = account_no
        self.__amount = amount
        DB_ins = revpayDB()
        self.__client = DB_ins.get_conn()
        self.__accounts_collection = DB_ins.get_collection('users_account')

    def withdraw(self):
        if self.__session_ins.isactive():
            if self.__amount <= 0:
                return jsonify({"error": "Deposit amount must be greater than zero"}), 400
            # Start a new session
            with self.__client.start_session() as session:
                # Start a new transaction within the session
                with session.start_transaction():
                    account = self.__accounts_collection.find_one({'user_id': self.__id}, session=session)
                    if account:
                        account_to_update = next((acc for acc in account['accounts'] if acc['account_number'] == self.__account_no), None)
                        if not account_to_update:
                            return jsonify({"error": "account not found"}), 404
                        if account_to_update['active'] == 0:
                            return jsonify({"message": "Account inactive!"}), 404
                        if self.__amount > account_to_update['balance']:
                            return jsonify({"error": "insuffcient balance"}), 404
                        new_balance = account_to_update['balance'] - self.__amount                    
                        self.__accounts_collection.update_one(
                            {'user_id': self.__id, 'accounts.account_number': self.__account_no}, 
                            {'$set': {'accounts.$.balance': new_balance}},  
                            session=session  
                        )
                        return jsonify({"message": "Withdrawal successful!", "current_balance": new_balance}),200
                    else:
                        return jsonify({"message": "Invalid Account number!"}), 404
        return jsonify({"message": "Please login to start transaction"})

    def deposit(self):
        if self.__session_ins.isactive():
            if self.__amount <= 0:
                return jsonify({"error": "Deposit amount must be greater than zero"}), 400
            # Start a new session
            with self.__client.start_session() as session:
                # Start a new transaction within the session
                with session.start_transaction():
                    account = self.__accounts_collection.find_one({'user_id': self.__id}, session=session)
                    if account:
                        account_to_update = next((acc for acc in account['accounts'] if acc['account_number'] == self.__account_no), None)
                        if not account_to_update:
                            return jsonify({"error": "account not found"}), 404
                        if account_to_update['active'] == 0:
                            return jsonify({"message": "Account inactive!"}), 404
                        new_balance = account_to_update['balance'] + self.__amount                    
                        self.__accounts_collection.update_one(
                            {'user_id': self.__id, 'accounts.account_number': self.__account_no}, 
                            {'$set': {'accounts.$.balance': new_balance}},  
                            session=session  
                        )
                        return jsonify({"message": "Deposit successful!", "current_balance": new_balance}),200
                    else:
                        return jsonify({"message": "Invalid Account number!"}), 404
        return jsonify({"message": "Please login to start transaction"})
