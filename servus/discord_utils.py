import aiohttp
from discord.ext import commands

async def createRequestsClient(bot:commands.Bot): 
    bot.session = aiohttp.ClientSession()

async def closeClient(aioclient:aiohttp.ClientSession):
    aioclient.close()