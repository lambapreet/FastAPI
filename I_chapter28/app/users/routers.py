from fastapi import APIRouter


router = APIRouter(prefix="/users")


@router.get("/",tags=['users'])
async def all_users():
    return {"msg":"users"}

@router.get("/{user_id}",tags=['users'])
async def get_user(user_id: int):
    return {"data":"return"}