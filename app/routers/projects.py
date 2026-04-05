from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.project import ProjectCreate, ProjectUpdate, ProjectOut
from app.services.project import (
    create_project,
    get_projects,
    get_project_by_id,
    update_project,
    delete_project
)
from app.auth.dependencies import get_current_user, role_required

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.post("/", response_model=ProjectOut)
def create(data: ProjectCreate, db: Session = Depends(get_db), user=Depends(role_required(["admin", "manager"]))):
    return create_project(db, data, user["id"])

@router.get("/", response_model=list[ProjectOut])
def list_projects(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_projects(db)

# @router.get("/", response_model=list[ProjectOut])
# def list_projects(db: Session = Depends(get_db), user=Depends(get_current_user)):
#     return get_projects(db)

@router.put("/{project_id}", response_model=ProjectOut)
def update(project_id: int, data: ProjectUpdate, db: Session = Depends(get_db), user=Depends(role_required(["admin", "manager"]))):
    project = update_project(db, project_id, data)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project

@router.delete("/{project_id}")
def delete(project_id: int, db: Session = Depends(get_db), user=Depends(role_required(["admin"]))):
    result = delete_project(db, project_id)

    if not result:
        raise HTTPException(status_code=404, detail="Project not found")

    return {"message": "Project deleted successfully"}

@router.get("/{project_id}", response_model=ProjectOut)
def get(project_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    project = get_project_by_id(db, project_id)

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project