from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from Authentication_api import Authentication
from Session import SessionManager
from Account import AccountManager
from Transaction import TransactionManager
from Balance import BalanceManager

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv('SECRET_KEY')

#register
@app.route("/register", methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    auth = Authentication(username,password)
    output = auth.register()
    return output

#login
@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    auth = Authentication(username,password)
    output = auth.login()
    return output

#logout
@app.route("/logout", methods=['POST'])
def logout():
    session = SessionManager()
    session.delete_session()
    return jsonify({'message': 'Logged out successfully!'})

#create account
@app.route("/createaccount", methods=['POST'])
def createaccount():
    account_number = request.form.get('account_no')
    ifsc_code = request.form.get('ifsc_code')
    acc = AccountManager(account_number,ifsc_code)
    output = acc.createaccount()
    return output

#transaction
@app.route("/transaction", methods=['POST'])
def transaction():
    #type -> deposit or withdrawal
    account_number = request.form.get('account_no')
    amount = request.form.get('amount')
    type = request.form.get('type')
    transaction_obj = TransactionManager(int(amount),account_number)
    output = ""
    if type == "withdraw":
       output = transaction_obj.withdraw()
    else:
       output = transaction_obj.deposit()
    return output

#balance
@app.route("/balance", methods=['POST'])
def Balance():
    account_number = request.form.get('account_no')
    balance_obj = BalanceManager(account_number)
    output = balance_obj.check_balance()
    return output

