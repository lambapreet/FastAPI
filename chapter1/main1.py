from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class ProductCategory(str, Enum):
    books = "Books"
    clothes = "clothes"
    mobile = "mobile"

@app.get("/product/{category}")
async def get_products(category: ProductCategory):
    if category == ProductCategory.books:
        return {"category": category, "message": "You selected books."}
    elif category == ProductCategory.clothes or category == ProductCategory.mobile:
        return {"category": category, "message": "You selected clothes or mobile."}
    else:
        return {"category": category, "message": "Other category."}


    