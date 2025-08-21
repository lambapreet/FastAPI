from models import User, Post
from db import SessionLocal
from sqlalchemy import insert, select, asc, desc, func


def create_user(name:str, email:str):
    with SessionLocal() as session:
        user = User(name=name, email=email)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
def create_post(user_id:int ,title:str, content:str):
    with SessionLocal() as session:
        post = Post(user_id=user_id,title=title, content=content)
        session.add(post)
        session.commit()
        
def get_user(user_id:int):
    with SessionLocal() as session:
        user = session.get_one(User, user_id)
        return user
    
def get_post(post_id:int):
    with SessionLocal() as session:
        statment = select(Post).where(Post.id == post_id)
        post = session.scalars(statment).one()
        return post
    
def all_user():
    with SessionLocal() as session:
        statment = select(User)
        users = session.scalars(statment).all()
        return users
    
def get_post_by_user(user_id:int):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        posts = user.posts if user else []
        return posts
    
def update_email(user_id:int, new_email:str):
    with SessionLocal() as session:
        user = session.get(User, user_id)
        if user:
            user.email = new_email
            session.commit()
        return user
    
def delete_post(post_id:int):
    with SessionLocal() as session:
        post = session.get(Post, post_id)
        if post:
            session.delete(post)
            session.commit()
            
def order_by_user():
    with SessionLocal() as session:
        statement = select(User).order_by(asc(User.name))
        users = session.scalars(statement).all()
        return users