from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional , Annotated


app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None

class Seller(BaseModel):
    username:str
    full_name: str    | None = None
    
# @app.post('/product')
# async def create_product(new_product: Product, seller:Optional[Seller]=None):
#     return {"new_product":new_product,"seller":seller}


@app.post('/product')
async def create_product(
    new_product: Product,
    seller: Seller,
    secret_key: Annotated[str, Body()]
):
    return {
        "new_product": new_product,
        "seller": seller,
        "secret_key": secret_key
    }