from fastapi import FastAPI, Request

app = FastAPI()

# Middleware that runs before and after every request
@app.middleware("http")
async def first_middleware(request: Request, call_next):
    
    print("Before")

    response = await call_next(request)  # process the request
    
    print("After")

    return response

@app.middleware("http")
async def Second_middleware(request: Request, call_next):
    
    print("2nd Before")

    response = await call_next(request)  # process the request
    
    print("2nd After")

    return response

# Example endpoint
@app.get("/user")
async def user():
    print("Endpoint called")
    return {"msg": "return"}
