from fastapi import FastAPI
from users.routers import router as user_router
from products.routers import router as product_router

app = FastAPI()

# app.include_router(user_router, tags=["users"])
# app.include_router(product_router, tags=["products"])


app.include_router(user_router )
app.include_router(product_router)


