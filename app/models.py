
from datetime import datetime
from uuid import uuid4

def create_user_dict(user_data, token):
    now = datetime.now()
    return {
        "id": str(uuid4()),
        "name": user_data.name,
        "email": user_data.email,
        "password": user_data.password,
        "phones": [phone.dict() for phone in user_data.phones],
        "created": now,
        "modified": now,
        "last_login": now,
        "token": token,
        "isactive": True
    }
