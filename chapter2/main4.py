from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional , Annotated


app = FastAPI()

class Category(BaseModel):
    name:str = Field(
        title="Category Name",
        max_length=50,
        min_length=10
    )
    description:str | None = Field(
        default=None,
        title="Description",
        max_length=100
    )

class Product(BaseModel):
    name:str =  Field(title="Product name",max_length=100, pattern="^[A-Za-z0-9]+$")
    price: float = Field(ge=1000)
    stock: int | None = Field(
        default=None,
        gt=0
    )
    category: Optional[Category] = Field(
        default=None,
        title="Product Category"
    )

@app.post('/product')
async def create_product(new_product: Product):
    return {"new_product":new_product} 