from sqlmodel import SQLModel,Field

class TaskBase(SQLModel):
    title:str
    content:str
    
class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class TaskPatch(SQLModel):
    title:str | None = None
    content:str | None = None
    
    
class TaskResponse(TaskBase):
    id:int

 
class Task(TaskBase,table=True):
    id: int = Field(primary_key=True)
