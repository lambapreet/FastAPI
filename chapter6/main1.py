from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

fruits = {"apple": "Red", "banana": "Yellow"}


class FruitException(Exception):
    def __init__(self, fruit_name: str):
        self.fruit_name = fruit_name


@app.exception_handler(FruitException)
async def fruit_exception(request: Request, exc: FruitException):
    return JSONResponse(
        status_code=418,
        content={"msg": f"{exc.fruit_name} is not valid value"}
    )


@app.get('/fruits/{id}')
async def get_fruit(id: str):
    if id not in fruits:
        raise FruitException(fruit_name=id)
    return fruits[id]
