from pydantic import BaseModel
from app.schemas.task import TaskOut

class ProjectCreate(BaseModel):
    title: str
    description: str | None = None

class ProjectUpdate(BaseModel):
    title: str | None = None
    description: str | None = None

class ProjectOut(BaseModel):
    id: int
    title: str
    description: str | None
    created_by: int
    # Relationships creator: str
    model_config = {"from_attributes": True}

class ProjectWithTasks(ProjectOut):
    tasks: list[TaskOut] = []