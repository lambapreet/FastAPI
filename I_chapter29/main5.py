from fastapi import FastAPI, Depends,HTTPException
from typing import Annotated


app = FastAPI()

class OwnerError(Exception):
    pass


def get_username():
    try:
        yield "Raj"
    except OwnerError as e:
        raise HTTPException(status_code=404,detail=f"{e} not found")
  
@app.get("item/{item_id}")  
def get_items(item_id:str, username:Annotated[str, Depends(get_username)]):
    data ={ "presser-cooker":{"description":"Essential for making", "owner":"Priya"}}
        
    
    if item_id not in data:
        raise HTTPException(status_code=404, detail="Item not found")
        
    item = data[item_id]
    
    if item["owner"] != username:
        raise OwnerError(username)
    
    return item