from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

from users.models import User
from products.models import Product
