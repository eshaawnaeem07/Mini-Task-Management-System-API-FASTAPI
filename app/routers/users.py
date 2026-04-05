from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.user import UserCreate,LoginRequest
from app.services.user import register_user, login_user
from app.auth.jwt import create_access_token, create_refresh_token
from fastapi import APIRouter, HTTPException
from app.auth.jwt import verify_token
router = APIRouter(tags=["Login & Registration"])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#REGISTER ENDPOINT
@router.post("/register")
def register(data: UserCreate, db: Session = Depends(get_db)):
    try:
        print("Registering user with email:", data.email)  # Debug statement
        return register_user(db, data)
    except Exception as e:
        return {"error": str(e)}
    
#LOGIN ENDPOINT
@router.post("/login")
def login(data: LoginRequest, db: Session = Depends(get_db)):
    try:
        user = login_user(db, data.email, data.password)
        if not user:
            return {"error": "Invalid credentials"}
        token = create_access_token({"id": user.id, "role": user.role})
        refresh_token = create_refresh_token({"id": user.id, "role": user.role})
        return {"access_token": token
                , "refresh_token": refresh_token
                , "token_type": "bearer"}
    except Exception as e:
        return {"error": str(e)}
    
#REFRESH TOKEN ENDPOINT
@router.post("/refresh")
def refresh_token(refresh_token: str):
    payload = verify_token(refresh_token)

    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_access_token = create_access_token({
        "id": payload["id"],
        "email": payload["email"],
        "role": payload["role"]
    })

    return {
        "access_token": new_access_token,
        "token_type": "bearer"
    }
