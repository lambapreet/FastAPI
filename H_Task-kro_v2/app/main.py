from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.config import create_tables
from app.task.services import *
from app.task.models import *

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.post("/task", response_model=TaskResponse)
def task_create(new_task:TaskCreate):
    task = create_task(title=new_task["title"], content=new_task["content"])
    return task

@app.get("/task",response_model=list[TaskResponse])
def get_all_task():
    task =  all_task()
    return task


@app.get("/task/{task_id}",response_model=TaskResponse)
def get_one_task(task_id:int):
    task = get_task()
    return task

@app.put("/task/{task_id}",response_model=TaskResponse)
def put_task(task_id:int, new_task:TaskUpdate):
    task = update_task(task_id, title=new_task["title"], content=new_task["content"])
    return task


@app.patch("/task/{task_id}",response_model=TaskResponse)
def patch_task(task_id:int, new_task:TaskPatch):
    task = patch_update(task_id, title=new_task.get("title"), content=new_task.get("content"))
    return task

@app.delete("/task/{task_id}",response_model=TaskResponse)
def task_delete(task_id:int):
    task = delete_task(task_id)
    return task