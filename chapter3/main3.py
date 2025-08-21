from fastapi import FastAPI, Body, Cookie, Header
from pydantic import BaseModel, Field
from typing import Optional , Annotated


app = FastAPI()

class Productheader(BaseModel):
    authorization: str
    accept_language: str
    x_tracking_id: list[str] = []
    
@app.get('product')
async def get_product(headers: Annotated[Productheader, Header()]):
    return {
        "headers":headers
    }