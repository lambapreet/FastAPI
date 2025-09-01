from sqlmodel import Session, select
from .models import Task, TaskResponse, TaskUpdate, TaskPatch
from app.db.config import engine
from fastapi import HTTPException



def create_task(session:Session,new_task: Task) -> TaskResponse:
    task = Task(title=new_task.title, content=new_task.content)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task
    
def all_task(session:Session,) -> list[TaskResponse]:
    stmt = select(Task)
    tasks = session.exec(stmt)
    return tasks.all()
    
    
def get_task(session:Session,task_id:int) -> TaskResponse:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        return task 
    
def update_task(session:Session,task_id:int, new_task: TaskUpdate) -> TaskResponse:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        task_data = new_task.model_dump()
        task.sqlmodel_update(task_data)
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
    
    
def patch_update(session:Session,task_id:int, new_task: TaskPatch) -> TaskResponse:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        task_data = new_task.model_dump(exclude_unset=True)
        task.sqlmodel_update(task_data)
        session.add(task)
        session.commit()
        session.refresh(task)
        return task
    
def delete_task(session:Session,task_id:int) -> TaskResponse:
        task = session.get(Task, task_id)
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        session.delete(task)
        session.commit()
        return task
        