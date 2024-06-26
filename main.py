import os
import asyncio
import discord

from discord.ext import commands
from dotenv import load_dotenv
from data import quotes

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
intents.message_content = True;

#uncomment this out if you would like for the bot to create a json file for you
#quotes.initializeJSON()

client = commands.Bot(command_prefix = "!", intents=intents)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Don's Adventure"))
    print(str(client.user) + " is now online!")
    

async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await client.load_extension(f"commands.{filename[:-3]}")
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
    

async def main():
    async with client:
        await load_extensions()
        await client.start(TOKEN)
asyncio.run(main())

