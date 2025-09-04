from fastapi import FastAPI, Depends
from typing import Annotated

app = FastAPI()



class CommonParameters:
    def __init__(self,q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit 
        
@app.get("/items")
async def read_items(common: Annotated[CommonParameters, Depends(CommonParameters)]):
    return common