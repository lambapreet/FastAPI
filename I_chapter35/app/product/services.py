from sqlmodel import Session, select
from fastapi import HTTPException
from .models import Product, ProductUpdate, ProductCreate, ProductPatch, ProductResponse


def create_product(session: Session, new_product: ProductCreate) -> ProductResponse:
    product = Product(title=new_product.title, description=new_product.description)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def all_products(session: Session) -> list[ProductResponse]:
    stmt = select(Product)
    products = session.exec(stmt).all()
    return products


def get_product(session: Session, product_id: int) -> ProductResponse:
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


def update_product(session: Session, product_id: int, new_data: ProductUpdate) -> ProductResponse:
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product_data = new_data.model_dump()  # ✅ Pydantic v2
    for key, value in product_data.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def patch_product(session: Session, product_id: int, new_data: ProductPatch) -> ProductResponse:
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product_data = new_data.model_dump(exclude_unset=True)  # ✅ partial update only
    for key, value in product_data.items():
        setattr(product, key, value)

    session.add(product)
    session.commit()
    session.refresh(product)
    return product


def delete_product(session: Session, product_id: int) -> ProductResponse:
    product = session.get(Product, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    session.delete(product)
    session.commit()
    return product
