from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session
from app.db.config import DependSession
from app.product.models import ProductCreate
from app.product.services import create_product, all_products

import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

# Mount static files
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory=TEMPLATE_DIR)


# Home page → loads the base template
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# HTMX → Product form
@app.get("/form", response_class=HTMLResponse)
def load_form(request: Request):
    return templates.TemplateResponse("product_form.html", {"request": request})


# HTMX → Product list
@app.get("/products", response_class=HTMLResponse)
def product_list(request: Request, session: DependSession):
    products = all_products(session)
    return templates.TemplateResponse(
        "product_list.html", {"request": request, "products": products}
    )


# HTMX → Create product and return updated list
@app.post("/products", response_class=HTMLResponse)
def product_create(
    request: Request,
    session: DependSession,
    title: str = Form(...),
    description: str = Form(...),
):
    product_data = ProductCreate(title=title, description=description)
    create_product(session, product_data)
    products = all_products(session)
    return templates.TemplateResponse(
        "product_list.html", {"request": request, "products": products}
    )
