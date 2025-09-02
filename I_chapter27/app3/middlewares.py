from fastapi import FastAPI, Request


# Middleware that runs before and after every request
async def first_middleware(request: Request, call_next):
    
    print("Before")

    response = await call_next(request)  # process the request
    
    print("After")

    return response

