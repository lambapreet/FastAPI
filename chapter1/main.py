from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def home():
    return {"message":"Hello"}

@app.get('/product')
async def all_products():
    return {'response':'All Products'}

@app.get('/product/{id}')
async def single_products(id:int):
    return {'response':'All Products','product':id}

@app.post('/product')
async def create_products(new_data:dict):
    return {'response':'All Products',"data":new_data}

@app.put('/product/{id}')
async def update_products(update_data:dict,id:int):
    return {'response':'All Products',"id":id,"data":update_data}

@app.patch('/product/{id}')
async def partial_products(update_data:dict,id:int):
    return {'response':'All Products',"id":id,"data":update_data}

@app.delete('/product/{id}')
async def delete_products(id:int):
    return {'response':'All Products','product':id}