


# Servus

A wrapper for the aiohttp library for making asynchronous web requests in Python.

Trying to preserve speed and flexibility provided by `aiohttp`, without sacrificing the human-friendliness of `requests`,  `servus` abstracts using client sessions and context managers when making asynchronous HTTP requests in Python.

Example usage:
```py
import servus
import aiohttp
import asyncio

async def main():
	# Create a new session
	mySession = aiohttp.ClientSession()
	
	# Use Servus to send a request. 
	# Servus automatically parses and serializes the response, and returns a ready to use object
	response = await servus.get(mySession, "http://httpbin.org")
	
	print(response.response) # (aiohttp.ClientResponse )
	print(response.json) # (dict)

	# Remeber to close the session!
	mySession.close()

asyncio.run(main())
```

`servus` also has inbuilt support for working with Discord bots. 

Example Usage:
```py
import discord
from discord.ext import commands
import asyncio
import servus
from servus.discord_utils import createRequestsClient

MY_TOKEN = "<YOUR_TOKEN>"
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))


@bot.command()
async  def hello(ctx):
	"""Hello world, with a HTTP request!"""
	r = await servus.get(bot.session,"https://httpbin.org")
	data = r.json
	await ctx.send(f"World! {data}")

# Add the createRequestClient coroutine to `bot` async loop
bot.loop.create_task(createRequestsClient(bot))

# Run the bot
bot.run(MY_TOKEN)
```
