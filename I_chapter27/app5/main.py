from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

app = FastAPI()

# app.add_middleware(HTTPSRedirectMiddleware)
app.add_middleware(TrustedHostMiddleware, allowed_host=["localhost","127.0.0.1"])

@app.get("/user")
async def user():
    print("Endpoint called")
    return {"msg": "return"}


# Example endpoint
@app.get("/product")
async def product():
    print("Endpoint Product")
    return {"msg 1": "return 1"}