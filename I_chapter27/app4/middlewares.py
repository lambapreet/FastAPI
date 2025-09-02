from fastapi import FastAPI, Request


# Middleware that runs before and after every request
async def user_middleware(request: Request, call_next):
    if request.url.path.startswith("/user"):
        print("Before")

        response = await call_next(request)  # process the request
        
        print("After")

        return response
    else:
        print(f"Skip middleware: {request.url.path}")
        response = await call_next(request)
        return response
    
async def product_middleware(request: Request, call_next):
    if request.url.path.startswith("/product"):
        print("Before Product")

        response = await call_next(request)  # process the request
        
        print("After Product")

        return response
    else:
        print(f"Skip middleware: {request.url.path}")
        response = await call_next(request)
        return response

