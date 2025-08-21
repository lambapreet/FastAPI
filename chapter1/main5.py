from fastapi import FastAPI, Query, Path
from typing import Annotated
from pydantic import AfterValidator


app = FastAPI()


PRODUCTS = [
    {'id':1,'name':'Dell','price':50000},
    {'id':2,'name':'HP','price':60000},
    {'id':3,'name':'ASUS','price':550000},
]


@app.get('/product')
async def get_product(search:str | None = None):
    if search:
        search_lower = search.lower()
        filter_product = []
        for product in PRODUCTS:
            if search_lower in product['name'].lower():
                filter_product.append(product)
        return filter_product
    return PRODUCTS

@app.get('/product')
async def get_product(search:str | None = Query(default=None, max_length=10)):
    if search:
        search_lower = search.lower()
        filter_product = []
        for product in PRODUCTS:
            if search_lower in product['name'].lower():
                filter_product.append(product)
        return filter_product
    return PRODUCTS


@app.get('/product')
async def get_product(
    search:Annotated[str | None, Query(max_length=100)] = None):
    if search:
        search_lower = search.lower()
        filter_product = []
        for product in PRODUCTS:
            if search_lower in product['name'].lower():
                filter_product.append(product)
        return filter_product
    return PRODUCTS

@app.get('/product')
async def get_product(
    search:
        Annotated[
            str,
            Path(ge=1),  
            Query(min_length=3, pattern="^[a-z]+$")
            ] = None
        ):
    if search:
        search_lower = search.lower()
        filter_product = []
        for product in PRODUCTS:
            if search_lower in product['name'].lower():
                filter_product.append(product)
        return filter_product
    return PRODUCTS


@app.get('/produuct')
async def get_product(search: Annotated[list[str] | None, Query()]=None):
    if search:
        filter_product = []
        for product in PRODUCTS:
            for s in search:
                if s.lower() in product['name'].lower():
                    filter_product.append(product)
            return filter_product
        return PRODUCTS

def check_valid_id(id: str):
    if not id.startswith("prod"):
        raise ValueError("Id must start with 'prod'")
    return id 

@app.get("/products")
async def get_products(id: Annotated[str | None, AfterValidator(check_valid_id)] = None):
    if id:
        return {'id': id, "message": "Valid Product ID"}
    return {"msg": "No ID provided"}