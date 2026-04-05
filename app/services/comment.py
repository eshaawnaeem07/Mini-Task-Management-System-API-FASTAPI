from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.comment import Comment

# Add comment to task with limit of 3 comments per user per task
def add_comment(db: Session, user_id, task_id, content):
    count = db.query(Comment).filter(
        Comment.user_id == user_id,
        Comment.task_id == task_id
    ).count()

    if count >= 3:
        raise Exception("Only 3 comments allowed per task")

    comment = Comment(
        content=content,
        task_id=task_id,
        user_id=user_id
    )
    db.add(comment)
    db.commit()
    return comment

# Get comments by task
def get_comments_by_task(db: Session, task_id: int):
    # return db.query(Comment).filter(Comment.task_id == task_id).all()
    # Only return comments that are not soft deleted
    return db.query(Comment).filter(
    Comment.task_id == task_id,
    Comment.is_deleted == False
).all()
#Delete comment
# def delete_comment(db: Session, comment_id: int, user):
#     comment = db.query(Comment).filter(Comment.id == comment_id).first()

#     if not comment:
#         raise HTTPException(status_code=404, detail="Comment not found")

#     # Only Admin or Owner can delete
#     if user["role"] != "admin" and comment.user_id != user["id"]: 
#         raise HTTPException(status_code=403, detail="Not authorized to delete this comment")

#     db.delete(comment)
#     db.commit()
#     return True
# Updated delete comment to support both hard delete (admin) and soft delete (manager)
def delete_comment(db: Session, comment_id: int, user):
    comment = db.query(Comment).filter(Comment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")

    # ADMIN (HARD DELETE)
    if user["role"] == "admin":
        db.delete(comment)
        db.commit()
        return "hard_deleted"

    # MANAGER (SOFT DELETE)
    elif user["role"] == "manager":
        comment.is_deleted = True
        db.commit()
        return "soft_deleted"
    else:
        raise HTTPException(status_code=403, detail="Only admin or manager can delete")
