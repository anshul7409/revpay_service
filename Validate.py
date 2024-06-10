import re
class Validate:
    def __init__(self,input):
        self.__input = input
    
    def validate(self):
        res = ""
        for key,value in self.__input.items():
            if  key == "amount":
                exp = r"^[1-9]\d*$"
                if not bool(re.match(exp, value)):
                   res = res + key + " (amount should be numberic)" +  " | " 
            if  key == "account_no":
                exp = r"^\d{10}(?!\d)$"
                if not bool(re.match(exp, value)):
                   res = res + key + " (acc should be numberic -> 10 digits)" + " | " 
            if  key == "ifsc_code":
                exp = r"^\d{8}(?!\d)$"
                if not bool(re.match(exp, value)):
                   res = res + key + " (ifsc code should be numberic -> 8 digits)" + " | "
            if  key == "username":
                exp = r"^[A-Za-z]+$"
                if not bool(re.match(exp, value)):
                   res = res + key + " (name should consists of characters)" +  " | "
            if  key == "password":
                exp = r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{1,16}$"
                if not bool(re.match(exp, value)):
                   res = res + key + " (password should consists of atleast 1 alphanumeric , 1 number)"  + " | "
        return res 