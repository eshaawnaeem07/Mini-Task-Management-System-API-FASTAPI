# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from app.database import Base

# class Task(Base):
#     __tablename__ = "tasks"

#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     description = Column(String)
#     status = Column(String)
#     project_id = Column(Integer, ForeignKey("projects.id"))
#     assigned_to = Column(Integer, ForeignKey("users.id"))
#     # RELATIONSHIPS
#     assignee = relationship("User", back_populates="assigned_tasks") #MANY TO ONE RELATIONSHIP WITH USER
#     project = relationship("Project", back_populates="tasks") #MANY TO ONE RELATIONSHIP WITH PROJECT
import enum
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.database import Base

class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

    status = Column(Enum(TaskStatus), default=TaskStatus.pending)

    # project_id = Column(Integer, ForeignKey("projects.id"))

    #apply ondelete="CASCADE" to automatically delete tasks when a project is deleted
    project_id = Column(Integer, ForeignKey("projects.id", ondelete="CASCADE"))
    # assigned_to = Column(Integer, ForeignKey("users.id"))

    #apply ondelete="SET NULL" to prevent deletion of tasks when a user is deleted, instead set assigned_to to NULL
    assigned_to = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    assignee = relationship("User", back_populates="assigned_tasks") #MANY TO ONE RELATIONSHIP WITH USER
    comments = relationship("Comment", back_populates="task", cascade="all, delete") #ONE TO MANY RELATIONSHIP WITH COMMENTS, cascade delete comments when task is deleted
    project = relationship("Project", back_populates="tasks") #MANY TO ONE RELATIONSHIP WITH PROJECT