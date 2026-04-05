from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    created_by = Column(Integer, ForeignKey("users.id"))
    #Relationships 
    owner = relationship("User", back_populates="projects") #MANY TO ONE RELATIONSHIP WITH USER
    tasks = relationship("Task", back_populates="project", cascade="all, delete") #ONE TO MANY RELATIONSHIP WITH TASKS, cascade delete tasks when project is deleted
    