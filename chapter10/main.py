from fastapi import FastAPI
from tabels import create_table
from services import row_sql

app = FastAPI()

create_table()


row_sql()

