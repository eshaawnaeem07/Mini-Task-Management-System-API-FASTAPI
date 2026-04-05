from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from app.auth.jwt import verify_token

security = HTTPBearer()

def get_current_user(token=Depends(security)):
    payload = verify_token(token.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid Token")
    return payload

def role_required(roles: list):
    def wrapper(user=Depends(get_current_user)):
        if user["role"] not in roles:
            raise HTTPException(status_code=403, detail="Access Denied")
        return user
    return wrapper