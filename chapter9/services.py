from db import engine
from tabels import users, post
from sqlalchemy import insert, select, asc, desc, func

def create_user(name:str, email:str):
    with engine.connect() as conn:
        stmt = insert(users).values(name=name, email=email)
        conn.execute(stmt)
        conn.commit()
        

def create_post(user_id:int, title:str, content:str):
    with engine.connect() as conn:
        stmt = insert(post).values(user_id=user_id,title=title,content=content)
        conn.execute(stmt)
        conn.commit()     
        

def order_user():
        with engine.connect() as conn:
                stmt = select(users).order_by(asc(post.c.id))
                result = conn.execute(stmt).fetchall()
                return result
        
def order_post():
        with engine.connect() as conn:
                stmt = select(post).order_by(desc(post.c.name))
                result = conn.execute(stmt).fetchall()
                return result
        

        
def count_post():
        with engine.connect() as conn:
                stmt = select(
                        post.c.user_id,
                        func.count(post.c.id).label("total post")
                ).group_by(post.c.user_id)
                result = conn.execute(stmt).fetchall()
                return result
        
        
def join_user():
        with engine.connect() as conn:
                stmt = select(
                        post.c.id,
                        post.c.title,
                        users.c.name.label("author")
                ).join(users, post.c.user_id == users.c.id)
                result = conn.execute(stmt).fetchall()
                return result