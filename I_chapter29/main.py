from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()


async def common_parameters(q:str | None=None, skip:int=0, limit:int=100):
    return {"q":q, "skip":skip, "limit":limit}



@app.get("/items")
async def read_items(common:Annotated[dict, Depends(common_parameters)]):
    return common


CommanDep = Annotated[dict, Depends(common_parameters)]

@app.get("/users")
async def read_users(common:CommanDep):
    return common
