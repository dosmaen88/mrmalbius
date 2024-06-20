# bot.py
import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
intents.message_content = True;

client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print(str(client.user) + " is now online!")

async def load_extensions():
    for filename in os.listdir("./commands"):
        if filename.endswith(".py"):
            await client.load_extension(f"commands.{filename[:-3]}")

async def main():
    async with client:
        await load_extensions()
        await client.start(TOKEN)
asyncio.run(main())

