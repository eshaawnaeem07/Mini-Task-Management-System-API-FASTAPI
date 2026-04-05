from fastapi import FastAPI
from app.database import Base, engine
from app.routers.users import router as user_router
from app.routers.projects import router as project_router
from app.routers.tasks import router as task_router
from app.routers.comments import router as comment_router


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router, prefix="/users")
app.include_router(project_router, prefix="/projects")
app.include_router(task_router, prefix="/tasks")
app.include_router(comment_router, prefix="/comments")