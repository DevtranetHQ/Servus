import aiohttp
from discord.ext import commands


async def createRequestsClient(bot: commands.Bot):
    """Create a new async client session for discord Bot instance."""
    bot.session = aiohttp.ClientSession()


async def closeClient(aioclient: aiohttp.ClientSession):
    """Close a Client Session. Abstraction of lower level session object close

    Parameters
    ----------
    aioclient : aiohttp.ClientSession
        Client Session to close
    """
    aioclient.close()
