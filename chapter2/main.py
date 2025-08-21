from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float
    stock: int | None = None



# @app.post('/product')
# async def create_product(new_product: Product):
#     return new_product


# @app.post('/product')
# async def create_product(new_product: Product):
#     product_dict = new_product.model_dump()
#     price_with_tax = new_product.price + (new_product.price * 18 / 100)
#     product_dict.update({"new_price":price_with_tax})
#     return product_dict

@app.put('/product/{prod_id}')
async def update_product(prod_id:int, new_product: Product, discount:float | None = None):
    return {"prod-id":prod_id, "new_product":new_product, "discount":discount}