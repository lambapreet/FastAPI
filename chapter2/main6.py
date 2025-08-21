from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Optional , Annotated


app = FastAPI()

class Product(BaseModel):
    id: int
    name: str = Field(examples=['Moto E'])
    price: float
    stock: int | None = None
    
    model_config = {
        "json_schema_extra": {
            "example": [
                {
                    "price":35.46,
                    "stock":4
                }
            ]
        }
    }


@app.post('/product')
async def create_product(new_product: Product):
    return {"new_product":new_product}
