from pydantic import BaseModel

class CommentCreate(BaseModel):
    content: str
    task_id: int

class CommentOut(BaseModel):
    id: int
    content: str
    task_id: int
    user_id: int
    # Relationships task: str
    # Relationships author: str
    model_config = {"from_attributes": True}