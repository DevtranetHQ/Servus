import aiohttp

class AioRequestsClient():
    def __init__(self, *args, **kwargs):
        self.session = aiohttp.ClientSession()

    async def get(self, url:str, **params):
        async with self.session.get(url, **params) as resp:
            return resp
    
    async def post(self, url, **params):
        async with self.session.post(url, **params) as resp:
            return resp

    async def put(self, url, **params):
        async with self.session.put(url, **params) as resp:
            return resp
    
    async def patch(self, url, **params):
        async with self.session.patch(url, **params) as resp:
            return resp
    
    async def delete(self, url, **params):
        async with self.session.delete(url, **params) as resp:
            return resp
    
    async def close_client(self):
        await self.session.close()
        