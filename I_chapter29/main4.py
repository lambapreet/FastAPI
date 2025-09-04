from fastapi import FastAPI, Depends, Header, HTTPException
from typing import Annotated

app = FastAPI()


async def veryfy_token(x_token:Annotated[str, Header()]):
    if x_token != "my-token":
        raise HTTPException(status_code=404,detail="Wrong X token")
    
@app.get("/items",dependencies=[Depends(veryfy_token)])
async def read_items():
    return {"msg":"data"}