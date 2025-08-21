from db import engine
from tabels import users, post
from sqlalchemy import insert, select, update,delete

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
        
def get_user(user_id:int):
       with engine.connect() as conn:
        stmt = select(users).where(users.c.id == user_id) 
        result = conn.execute(stmt).mappings().fetchone()  
        return dict(result) if result else None
    
def get_all():
       with engine.connect() as conn:
        stmt = select(users)
        result = conn.execute(stmt).mappings().fetchall()  
        return list(map(dict, result))

def get_post(user_id: int):
       with engine.connect() as conn:
        stmt = select(post).where(post.c.id == user_id)
        result = conn.execute(stmt).mappings().fetchall()  
        return list(map(dict, result))
    

def update_user(user_id: int, new_email:str):
       with engine.connect() as conn:
        stmt = update(users).where(users.c.id == user_id).values(email = new_email)
        conn.execute(stmt) 
        conn.commit()
        
def delete_post(post_id: int):
       with engine.connect() as conn:
        stmt = delete(post).where(post.c.id == post)
        conn.execute(stmt) 
        conn.commit()