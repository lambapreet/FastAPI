from fastapi import FastAPI, HTTPException


app = FastAPI()


items =  {"apple":"Red","banana":"yellow"}


@app.get('/items/{id}')
async def get_item(id:str):
    if id not in items:
        raise HTTPException(status_code=404, detail="Item not found",headers={"error":"item missing"})
    return items[id]