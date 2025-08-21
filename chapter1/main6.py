from fastapi import FastAPI, Query, Path
from typing import Annotated
from pydantic import AfterValidator


app = FastAPI()


PRODUCTS = [
    {'id':1,'name':'Dell','price':50000},
    {'id':2,'name':'HP','price':60000},
    {'id':3,'name':'ASUS','price':550000},
]


@app.get("/product/{id}")
async def get_product(id: Annotated [int, Path(ge=1) ]):
    for product in PRODUCTS:
        if product['id'] == id:
            return product
    return {'error':'invalid input'}

@app.get('/product/{id}')
async def get_product(
    id:Annotated[int, Path(ge=1)],
    search:Annotated[str | None, Query(max_length=100)] = None):
    if search:
        search_lower = search.lower()
        filter_product = []
        for product in PRODUCTS:
            if search_lower in product['name'].lower():
                filter_product.append(product)
        return filter_product
    return PRODUCTS