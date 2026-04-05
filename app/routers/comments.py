from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.comment import CommentCreate, CommentOut
from app.services.comment import (
    add_comment,
    get_comments_by_task,
    delete_comment
)
from app.auth.dependencies import get_current_user

router = APIRouter(prefix="/comments", tags=["Comments"])

# Add comment to task
@router.post("/", response_model=CommentOut)
def add(data: CommentCreate,
        db: Session = Depends(get_db),
        user=Depends(get_current_user)):
    try:
        return add_comment(db, user["id"], data.task_id, data.content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Get comments for a task 
@router.get("/task/{task_id}", response_model=list[CommentOut])
def get_task_comments(task_id: int,
                      db: Session = Depends(get_db),
                      user=Depends(get_current_user)):
    return get_comments_by_task(db, task_id)

# Delete comment
@router.delete("/{comment_id}")
@router.delete("/{comment_id}")
def delete(comment_id: int,
           db: Session = Depends(get_db),
           user=Depends(get_current_user)):

    result = delete_comment(db, comment_id, user)

    if result == "hard_deleted":
        return {"message": "Comment permanently deleted (Admin)"}

    elif result == "soft_deleted":
        return {"message": "Comment soft deleted (Manager)"}