class Schema:
    def __init__(self,name):
        self.__name = name 
    
    def get_schema(self):
        if self.__name == 'users_collection':
            return {
                "bsonType": "object",
                "required": ["username", "password"],
                "properties": {
                    "username": {
                        "bsonType": "string",
                    },
                    "password": {
                        "bsonType": "string",
                    }
                }
            }
        elif self.__name == 'users_account':
            return {
                "bsonType": "object",
                "required": ["user_id", "accounts"],
                "properties": {
                    "user_id": {
                        "bsonType": "string",
                        "description": "must be a string and is required"
                    },
                    "accounts": {
                        "bsonType": "array",
                        "minItems": 1,
                        "items": {
                            "bsonType": "object",
                            "required": ["UID", "account_number", "ifsc_code", "balance", "active"],
                            "properties": {
                                "UID": {
                                    "bsonType": "string",
                                    "description": "must be a string and is required"
                                },
                                "account_number": {
                                    "bsonType": "string",
                                    "description": "must be a string and is required"
                                },
                                "ifsc_code": {
                                    "bsonType": "string",
                                    "description": "must be a string and is required"
                                },
                                "balance": {
                                    "bsonType": ["int", "double"],
                                    "minimum": 0,
                                    "description": "must be a number with a minimum value of 0 and is required"
                                },
                                "active": {
                                    "bsonType": "int",
                                    "enum": [0, 1],
                                    "description": "must be an integer and is required"
                                }
                            }
                        }
                    }
                }
            }
