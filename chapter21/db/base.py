from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import models at the end (after Base is defined)
from users import models  # noqa: F401
from products import models  # noqa: F401
