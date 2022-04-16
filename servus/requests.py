from aiohttp import ClientSession
from . import __utils as _utils

async def get(session:ClientSession, url:str, **params):
    async with session.get(url, **params) as resp:
        fresp = await _utils.parseResponse(resp)
    return fresp
    
async def post(session:ClientSession, url, **params):
    async with session.post(url, **params) as resp:
        fresp = await _utils.parseResponse(resp)
    return fresp

async def put(session:ClientSession, url, **params):
    async with session.put(url, **params) as resp:
        fresp = await _utils.parseResponse(resp)
    return fresp

async def patch(session:ClientSession, url, **params):
    async with session.patch(url, **params) as resp:
        fresp = await _utils.parseResponse(resp)
    return fresp

async def delete(session:ClientSession, url, **params):
    async with session.delete(url, **params) as resp:
        fresp = await _utils.parseResponse(resp)
    return fresp

    