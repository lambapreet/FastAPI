from models import User
from db import async_session
from sqlalchemy import select, update, delete


# ✅ Create user
async def create_user(name: str, email: str):
    async with async_session() as session:
        user = User(name=name, email=email)
        session.add(user)
        await session.commit()
        await session.refresh(user)  # so we get the new ID
        return user


# ✅ Get all users
async def get_all_users():
    async with async_session() as session:
        result = await session.execute(select(User))
        return result.scalars().all()


# ✅ Get single user by ID
async def get_user_by_id(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()


# ✅ Update user email
async def update_user_email(user_id: int, new_email: str):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            user.email = new_email
            await session.commit()
            await session.refresh(user)
            return user
        return None


# ✅ Delete user
async def delete_user(user_id: int):
    async with async_session() as session:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            await session.delete(user)
            await session.commit()
            return True
        return False
