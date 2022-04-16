import aiohttp
from .models import AioHttpResponseWrapper, RESPONSE_PROPS
import json

async def parseResponse(resp:aiohttp.ClientResponse):
    data = dict().fromkeys(RESPONSE_PROPS, {})

    data["response"] = resp
    try:
        data["json"] = await resp.json()
    except:
        pass
    try:
        data["txt"] = await resp.txt()
    except:
        pass
    try:
        data["data"] = await resp.data()
    except:
        pass
    return AioHttpResponseWrapper(**data)