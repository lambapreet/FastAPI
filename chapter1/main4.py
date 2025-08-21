from fastapi import FastAPI


app = FastAPI()


@app.get('/index')
async def index(product:str):
    return {'status':'ok','product':product}


@app.get('/index')
async def index1(product:str,limit:int):
    return {'status':'ok','product':product,'limit':limit}

@app.get('/index')
async def index(product:str,limit:int=10):
    return {'status':'ok','product':product,'limit':limit}

@app.get('/index')
async def index(limit:int,product:str=None):
    return {'status':'ok','product':product,'limit':limit}


@app.get('/index/{id}')
async def index(id:int,product:str):
    return {'status':'ok','id':id,'product':product}