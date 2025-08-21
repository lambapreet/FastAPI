from fastapi import FastAPI, Body, Cookie
from pydantic import BaseModel, Field
from typing import Optional , Annotated,List


app = FastAPI()


class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None

class ProductOut(BaseModel):
    name: str
    price: float   
    
# Return Type Annotation
@app.get('/product')
async def product() -> Product:
    return {'id':1, "name":"Moto E", 'price':33.5, 'stock':5}


@app.get('/products')
async def all_product() -> List[Product]:
    return [
        {'id':1, "name":"Moto E", 'price':33.5, 'stock':5},
        {'id':2, "name":"Moto G", 'price':37.5, 'stock':6}
    ]

@app.post('/products')
async def create_product(product: Product) -> Product:
    return product
    
@app.post('/product')
async def Fix_product(product: Product) -> ProductOut:
    return product