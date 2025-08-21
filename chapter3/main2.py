from fastapi import FastAPI, Body, Header
from pydantic import BaseModel, Field
from typing import Optional , Annotated


app = FastAPI()

@app.get('products')
async def get_products(user_agent: Annotated[str | None, Header()] = None):
    return user_agent


# curl -H "User-Agent: Mozilla/5.0" http://127.0.0.1:8000/products


