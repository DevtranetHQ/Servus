import aiohttp
import servus
import discord
from discord.ext import commands
import asyncio
import servus

MY_TOKEN = "OTQzMjAxMTk0MDA2OTYyMjE4.YgvmkA.jitbaVT5oltkkwtduHDeai_ZxLQ"

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))

@bot.event
async def on_ready():
    """On ready event!"""
    print("Logged in as " + str(bot.user))
    print("User ID: " + str(bot.user.id))
    r = await servus.get(bot.session,"https://reqres.in/api/users?page=2")
    print(r)

    print("Ready!")



@bot.command()
async def ping(ctx):
    """Ping pong!"""
    latency = ctx.bot.latency
    latency = latency * 1000
    latency = round(latency)
    await ctx.send("Pong! My ping is **{}ms**!".format(latency))

@bot.command()
async def hello(ctx):
    """Hello world!"""
    r = await servus.get(bot.session,"https://reqres.in/api/users?page=2")
    print(r)
    data = r.json
    await ctx.send(f"World! {data}")

@bot.command()
async def world(ctx):
    """World, hello!"""
    await ctx.send("Hello!")

@bot.command()
async def slap(ctx, user: discord.Member=None):
    if user is None:
        message = "I don't wanna slap you!"
    else:
        message = "{} was slapped by {}! *ouch*".format(ctx.author.mention,
                                                        user.mention)
    await ctx.send(message)


bot.loop.create_task(servus.discord_utils.createRequestsClient(bot))
bot.run(MY_TOKEN)
