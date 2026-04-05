from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Boolean

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    content = Column(String)
    # cascade delete when task is deleted
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"))
    #cascade delete when user is deleted
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    # for soft delete
    is_deleted = Column(Boolean, default=False)
    # RELATIONSHIPS
    author = relationship("User", back_populates="comments") #MANY TO ONE RELATIONSHIP WITH USER
    task = relationship("Task", back_populates="comments") #MANY TO ONE RELATIONSHIP WITH TASK