from fastapi import FastAPI, Body, Cookie
from pydantic import BaseModel, Field
from typing import Optional , Annotated,List


app = FastAPI()

product_db = {
    "1":{'id':'1',"name":"Dell",'price':50000,'stocl':5},
    "2":{'id':'2',"name":"HP",'price':70000,'stocl':15},
}

class Product(BaseModel):
    id: str
    name: str
    price: float
    des: Optional[str] = None
    tax: float = 15.0
    
@app.get('/product/{id}',response_model=Product,response_model_exclude_unset=True)
async def product(id:str):
    return product_db.get(id, {})
