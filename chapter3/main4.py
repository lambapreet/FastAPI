from fastapi import FastAPI, Body, Cookie, Header
from pydantic import BaseModel, Field
from typing import Optional , Annotated


app = FastAPI()

class Products(BaseModel):
    model_config = {"extra":"forbid"}
    session_id : str = Field(title="Session_id")
    preferred_category: str | None =  Field(default=None, title="Prefered Category")
    tracking_id : str | None = None
    
class PriceFilter(BaseModel):
    min_price: float = Field(ge=0, title="Minimum Price")
    max_price: float | None = Field(default=None, title="Maximum Price")
    
class Productheader(BaseModel):
    authorization: str
    accept_language: str
    
@app.get("products")
async def get_products(cookies: Annotated[Products, Cookie()],
                       price_filter: Annotated[PriceFilter, Body(embed=True)],
                       headers:Annotated[Productheader, Header()]):
    
    response = {"session id":cookies.session_id}
    if cookies.preferred_category:
        response["message"] = f"Recommendation for {cookies.preferred_category} product"
    response["price_range"] = {"min_price":price_filter.min_price,
                               "max_price":price_filter.max_price}
    response["message"] = f"session {cookies.session_id} with price {price_filter.min_price} to {price_filter.max_price}"
    return {"response":response, "header":headers}