from fastapi import FastAPI
from .middlewares import first_middleware

app = FastAPI()

app.middleware("http")(first_middleware)

# Example endpoint
@app.get("/user")
async def user():
    print("Endpoint called")
    return {"msg": "return"}
