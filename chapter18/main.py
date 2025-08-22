from models import create_tables
import asyncio
from services import *

async def main():
    
    # await create_tables()
    
    
    await create_user("raaj","raaj@emaple.com")
    
    
asyncio.run(main())