from fastapi import FastAPI, Request

app = FastAPI()

# Middleware that runs before and after every request
@app.middleware("http")
async def first_middleware(request: Request, call_next):
    print(f"Request: {request.method} {request.url}")   # fixed "Reguest" → "Request"

    response = await call_next(request)  # process the request

    print(f"Status code: {response.status_code}")  # log status code

    return response

# Example endpoint
@app.get("/user")
async def user():
    print("Endpoint called")
    return {"msg": "return"}
