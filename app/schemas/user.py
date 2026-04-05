from pydantic import BaseModel, EmailStr, field_validator
from app.models.user import UserRole

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    confirm_password: str
    role: UserRole = UserRole.employee

    # Validation: passwords must match
    @field_validator("confirm_password")
    def passwords_match(cls, v, info):
        if "password" in info.data and v != info.data["password"]:
            raise ValueError("Passwords do not match")
        return v
    
class UserOut(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: UserRole
    # Relationships projects: list[str] = []
    model_config = {"from_attributes": True}

class LoginRequest(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class RefreshTokenRequest(BaseModel):
    refresh_token: str