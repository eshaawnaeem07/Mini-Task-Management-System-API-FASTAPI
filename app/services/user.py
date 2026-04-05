from sqlalchemy.orm import Session
from app.models.user import User
from passlib.context import CryptContext

pwd = CryptContext(schemes=["bcrypt"]) #PASSWORD HASHING CONTEXT
#USER SERVICES FOR REGISTRATION AND LOGIN
def register_user(db: Session, data):
    try:
        existing_user = db.query(User).filter(User.email == data.email).first()
        if existing_user:
            raise Exception("Email already registered")

        user = User(
            name=data.name,
            email=data.email,
            password=pwd.hash(data.password),  # only password
            role=data.role
        )

        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except Exception as e:
        raise e
    
def login_user(db: Session, email, password):
    user = db.query(User).filter(User.email == email).first()
    if user and pwd.verify(password, user.password):
        return user
    return None