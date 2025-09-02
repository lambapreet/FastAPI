from fastapi import FastAPI
from .middlewares import user_middleware,product_middleware

app = FastAPI()

app.middleware("http")(user_middleware)
app.middleware("http")(product_middleware)

# Example endpoint
@app.get("/user")
async def user():
    print("Endpoint called")
    return {"msg": "return"}


# Example endpoint
@app.get("/product")
async def product():
    print("Endpoint Product")
    return {"msg 1": "return 1"}