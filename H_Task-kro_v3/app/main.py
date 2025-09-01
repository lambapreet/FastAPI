from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import create_tables, DependSession
from app.task.services import *
from app.task.models import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.post("/task", response_model=TaskResponse)
def task_create(session: DependSession,new_task:TaskCreate):
    task = create_task(session, new_task)
    return task

@app.get("/task",response_model=list[TaskResponse])
def get_all_task(session: DependSession,):
    task =  all_task(session)
    return task


@app.get("/task/{task_id}",response_model=TaskResponse)
def get_one_task(session: DependSession,task_id:int):
    task = get_task(session)
    return task

@app.put("/task/{task_id}",response_model=TaskResponse)
def put_task(session: DependSession,task_id:int, new_task:TaskUpdate):
    task = update_task(session,task_id, new_task)
    return task


@app.patch("/task/{task_id}",response_model=TaskResponse)
def patch_task(session: DependSession,task_id:int, new_task:TaskPatch):
    task = patch_update(session,task_id,new_task)
    return task

@app.delete("/task/{task_id}",response_model=TaskResponse)
def task_delete(session: DependSession,task_id:int):
    task = delete_task(session,task_id)
    return task