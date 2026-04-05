from sqlalchemy.orm import Session
from app.models.project import Project

def create_project(db: Session, data, user_id):
    project = Project(
        title=data.title,
        description=data.description,
        created_by=user_id
    )
    db.add(project)
    db.commit()
    db.refresh(project)
    return project


def get_projects(db: Session):
    return db.query(Project).all()

def get_project_by_id(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()

def update_project(db: Session, project_id: int, data):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return None

    if data.title:
        project.title = data.title
    if data.description:
        project.description = data.description

    db.commit()
    db.refresh(project)
    return project

def delete_project(db: Session, project_id: int):
    project = db.query(Project).filter(Project.id == project_id).first()

    if not project:
        return None

    db.delete(project)
    db.commit()
    return True