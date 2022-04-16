from . import aioclient

async def getClient():
    return aioclient.AioRequestsClient()
