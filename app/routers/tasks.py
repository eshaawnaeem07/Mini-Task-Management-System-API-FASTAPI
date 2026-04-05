from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.task import (
    TaskCreate,
    TaskUpdate,
    TaskAssign,
    TaskStatusUpdate,
    TaskOut
)
from app.services.task import (
    create_task,
    get_tasks,
    get_task_by_id,
    update_task,
    assign_task,
    update_status,
    delete_task
)
from app.auth.dependencies import get_current_user, role_required

router = APIRouter(prefix="/tasks", tags=["Tasks"])
# Create task
@router.post("/", response_model=TaskOut)
def create(data: TaskCreate,
           db: Session = Depends(get_db),
           user=Depends(role_required(["admin", "manager"]))):
    return create_task(db, data)
#list tasks
@router.get("/", response_model=list[TaskOut])
def list_tasks(db: Session = Depends(get_db),
    user=Depends(get_current_user)):
    return get_tasks(db)

#get task by id
@router.get("/{task_id}", response_model=TaskOut)
def get(task_id: int,
        db: Session = Depends(get_db),
        user=Depends(get_current_user)):
    task = get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task
#update task
@router.put("/{task_id}", response_model=TaskOut)
def update(task_id: int,
           data: TaskUpdate,
           db: Session = Depends(get_db),
           user=Depends(role_required(["admin", "manager"]))):
    task = update_task(db, task_id, data)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task
#assign task
@router.patch("/{task_id}/assign", response_model=TaskOut)
def assign(task_id: int,
           data: TaskAssign,
           db: Session = Depends(get_db),
           user=Depends(role_required(["admin", "manager"]))):
    task = assign_task(db, task_id, data.assigned_to)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task
#update status 
@router.patch("/{task_id}/status", response_model=TaskOut)
def update_task_status(task_id: int,
                       data: TaskStatusUpdate,
                       db: Session = Depends(get_db),
                       user=Depends(get_current_user)):
    try:
        task = update_status(db, task_id, data.status, user)

        if not task:
            raise HTTPException(status_code=404, detail="Task not found")

        return task

    except Exception as e:
        raise HTTPException(status_code=403, detail=str(e))
#delete task
@router.delete("/{task_id}")
def delete(task_id: int,
           db: Session = Depends(get_db),
           user=Depends(role_required(["admin", "manager"]))):
    result = delete_task(db, task_id)

    if not result:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}