from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum

# Enum for roles
class UserRole(str, enum.Enum):
    admin = "admin"
    manager = "manager"
    employee = "employee"

class User(Base):
    __tablename__ = "users"

    # PRIMARY KEY
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    #UNIQUE EMAIL
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(Enum(UserRole), default=UserRole.employee, nullable=False)

    # Relationships
    projects = relationship("Project", back_populates="owner")#ONE TO MANY RELATIONSHIP WITH PROJECTS
    # assigned_tasks = relationship("Task", back_populates="assignee") #ONE TO MANY RELATIONSHIP WITH TASKS
    # comments = relationship("Comment", back_populates="author") #ONE TO MANY RELATIONSHIP WITH COMMENTS
    assigned_tasks = relationship("Task", back_populates="assignee") #ONE TO MANY RELATIONSHIP WITH TASKS, cascade delete tasks when user is deleted
    comments = relationship("Comment", back_populates="author", cascade="all, delete") #ONE TO MANY RELATIONSHIP WITH COMMENTS, cascade delete comments when user is deleted