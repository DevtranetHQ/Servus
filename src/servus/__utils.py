import aiohttp
from .models import AioHttpResponseWrapper, RESPONSE_PROPS
import json


async def parseResponse(resp: aiohttp.ClientResponse):
    """Extract response object properties so they can be accessed synchronously e.g JSON, text and Binary data fields

    Parameters
    ----------
    resp : aiohttp.ClientResponse
        Async Response object

    Returns
    -------
    AioHttpResponseWrapper
        Wrapped response that provides synchronous access response properties
    """

    # Create data with default values
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

    # Create a new ResponseWrapper and pass in extracted values
    return AioHttpResponseWrapper(**data)
