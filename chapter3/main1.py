from fastapi import FastAPI, Body, Cookie
from pydantic import BaseModel, Field
from typing import Optional , Annotated


app = FastAPI()

class ProductCookies(BaseModel):
    model_config = {"extra":"forbid"}
    session_id : str
    preferred_category: str | None = None
    tracking_id : str | None = None
    
    
@app.get('/products')
async def get_cookies(cookies: Annotated[ProductCookies, Cookie()]):
    respose = {"session_id": cookies.session_id}
    if cookies.preferred_category:
        respose["message"] = f"Recommendation for {cookies.preferred_category} product"
    else:
        respose["message"] = f"Recommendation for session id {cookies.session_id} product"
    if cookies.tracking_id:
        respose["message"] = f"Recommendation for tracking id {cookies.tracking_id} product"
    return respose