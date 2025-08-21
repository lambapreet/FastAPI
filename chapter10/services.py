from db import engine
from tabels import users, post
from sqlalchemy import text

def row_sql():
    with engine.connect() as conn:
        statement = text('''
                         INSERT INTO users(name, email)
                         VALUES(:name, :email)
                         ''')
        conn.execute(statement, {"name": "sonam", "email": "sonam@gmail.com"})
        conn.commit()
