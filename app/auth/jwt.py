from jose import jwt
from datetime import datetime, timedelta

SECRET = "secret123"
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE = 2  # hours
REFRESH_TOKEN_EXPIRE = 7  # days


def create_access_token(data: dict):
    data = data.copy()
    data.pop("password", None)

    data.update({
        "exp": datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE),
        "type": "access"
    })

    return jwt.encode(data, SECRET, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
    data = data.copy()
    data.pop("password", None)

    data.update({
        "exp": datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE),
        "type": "refresh"
    })

    return jwt.encode(data, SECRET, algorithm=ALGORITHM)


def verify_token(token: str):
    try:
        return jwt.decode(token, SECRET, algorithms=[ALGORITHM])
    except:
        return None