from fastapi import FastAPI
from contextlib import asynccontextmanager
from db.config import create_tables, DependSession
from product.services import *
from product.models import *


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/products", response_model=ProductResponse)
def create_product_api(session: DependSession, new_product: ProductCreate):
    product = create_product(session, new_product)
    return product


@app.get("/products", response_model=list[ProductResponse])
def get_all_products_api(session: DependSession):
    products = all_products(session)
    return products


@app.get("/products/{product_id}", response_model=ProductResponse)
def get_one_product_api(session: DependSession, product_id: int):
    product = get_product(session, product_id)
    return product


@app.put("/products/{product_id}", response_model=ProductResponse)
def update_product_api(session: DependSession, product_id: int, new_data: ProductUpdate):
    product = update_product(session, product_id, new_data)
    return product


@app.patch("/products/{product_id}", response_model=ProductResponse)
def patch_product_api(session: DependSession, product_id: int, new_data: ProductPatch):
    product = patch_product(session, product_id, new_data)
    return product


@app.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product_api(session: DependSession, product_id: int):
    product = delete_product(session, product_id)
    return product
