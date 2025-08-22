from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///D:/FASTAPI/chapter15/test.db"


engine = create_async_engine(DATABASE_URL, echo=True, future=True)
