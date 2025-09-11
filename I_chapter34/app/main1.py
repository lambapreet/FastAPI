from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from sqlmodel import Session, select
from app.db.config import engine, DependSession
from app.product.models import Product, ProductCreate
from app.product.services import create_product

import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


# Jinja2 templates
templates = Jinja2Templates(directory=TEMPLATE_DIR)


@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    with Session(engine) as session:
        products = session.exec(select(Product)).all()
    return templates.TemplateResponse(
        "products_list.html",
        {"request": request, "products": products}
    )


@app.post("/create", response_class=HTMLResponse)
def create(
    request: Request,
    session: DependSession,
    title: str = Form(...),
    description: str = Form(...)
):
    new_product = ProductCreate(title=title, description=description)
    create_product(session, new_product)
    return RedirectResponse("/", status_code=302)
