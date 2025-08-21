from fastapi import FastAPI, Body, Cookie
from pydantic import BaseModel, Field
from typing import Optional , Annotated,List


app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None

class ProductOut(Product):
    des: str 
    
# Response Model
@app.get('/product',response_model=Product)
async def product():
    return {'id':1, "name":"Moto E", 'price':33.5, 'stock':5}

@app.post('/products',response_model=Product)
async def create_product(product: Product):
    return product

@app.post('/user',response_model=ProductOut)
async def create_product(product: Product):
    return product