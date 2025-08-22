from tables import create_table
import asyncio
from services import create_user

async def main():
    # await create_table()
    
    await create_user("sonam", "sonam@gmail.com")
    
    
    
asyncio.run(main())