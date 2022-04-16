import asyncio
import servus    
import aiohttp


async def main():
    session = aiohttp.ClientSession()
    r = await servus.get(session,"https://reqres.in/api/users?page=2")
    print(type(r.json))
    

asyncio.run(main())