from fastapi import APIRouter


router = APIRouter(tags=["products"])


@router.get("/products")
async def all_users():
    return {"msg":"users"}

@router.get("/products/{product_id}")
async def get_user(product_id: int):
    return {"data":"return"}