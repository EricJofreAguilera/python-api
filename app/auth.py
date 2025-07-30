
from jose import jwt
from datetime import datetime, timedelta
from uuid import uuid4

SECRET_KEY = "secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_token(email: str):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": email, "exp": expire, "jti": str(uuid4())}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
