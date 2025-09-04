from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()

# Dependency function
async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

# Another dependency that depends on common_parameters
async def main_parameters(user: Annotated[dict, Depends(common_parameters)]):
    return {"user": user, "role": "admin"}

# Route using the dependency
@app.get("/items/")
async def read_items(params: Annotated[dict, Depends(main_parameters)]):
    return params
