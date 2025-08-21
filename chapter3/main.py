from fastapi import FastAPI, Body, Cookie
from pydantic import BaseModel, Field
from typing import Optional , Annotated


app = FastAPI()


@app.get('/products')
async def get_session(session_id: Annotated[str | None, Cookie()] = None):
    if session_id:
        return {"message":f"Recommendations for session {session_id}","session_id":session_id}
    return {"msg":"No session"}