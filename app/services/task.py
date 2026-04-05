from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.task import Task

def create_task(db: Session, data):
    try:
        task = Task(
            title=data.title,
            description=data.description,
            status="pending",
            project_id=data.project_id,
            assigned_to=data.assigned_to
        )
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def get_tasks(db: Session):
    try:
        return db.query(Task).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_task_by_id(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

def update_task(db: Session, task_id: int, data):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    try:
        if data.title:
            task.title = data.title
        if data.description:
            task.description = data.description

        db.commit()
        db.refresh(task)
        return task

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))


def assign_task(db: Session, task_id: int, user_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    try:
        task.assigned_to = user_id
        db.commit()
        db.refresh(task)
        return task
    
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def update_status(db: Session, task_id: int, status, user):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Authorization check
    if user["role"] != "admin" and task.assigned_to != user["id"]:
        raise HTTPException(status_code=403, detail="Not authorized")
    try:
        task.status = status
        db.commit()
        db.refresh(task)
        return task

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    try:
        db.delete(task)
        db.commit()
        return {"message": "Task deleted successfully"}

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))