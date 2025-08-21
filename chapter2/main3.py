from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional , Annotated


app = FastAPI()

class Product(BaseModel):
    id: int
    name:str =  Field(title="Product name",max_length=100, pattern="^[A-Za-z0-9]+$")
    price: float = Field(ge=1000)

    
@app.post('/product')
async def create_product(new_product: Product):
    return {"new_product":new_product} 