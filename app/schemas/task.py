from pydantic import BaseModel
from typing import Optional
from app.models.task import TaskStatus

class TaskCreate(BaseModel):
    title: str
    description: str
    project_id: int
    assigned_to: int

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class TaskAssign(BaseModel):
    assigned_to: int

class TaskStatusUpdate(BaseModel):
    status: TaskStatus

class TaskOut(BaseModel):
    id: int
    title: str
    description: str
    status: TaskStatus
    project_id: Optional[int] = None
    assigned_to: Optional[int] = None
    # Relationships project: str
    # Relationships assignee: str
    model_config = {"from_attributes": True}