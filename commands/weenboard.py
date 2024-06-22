from discord.ext import commands
import random
import requests
import discord
MAX_PAGE = 155
BASE_URL = 'https://territorial.io/clans'
IMG_URL =  'https://yt3.googleusercontent.com/BVF24poGwihsMBMwF-p2MHC5WyQMLLhRU0sZALBrYQlDyQw1T8Gze4AwTQCP50Esk1b7z0CS=s160-c-k-c0x00ffffff-no-rj'
WORD = "ween,"
PREFIX = "b'"
scores = []

@commands.command()
async def weenboard(ctx):
    r = requests.get(BASE_URL, stream=True)

    for line in r.iter_lines():
        if WORD in str(line).lower().split():
            scores.append(line)
    msg = str(scores[0]).replace(PREFIX, "")
    print(msg)
    components = msg.split(", ")
    print(components)
    leaderloc = components[0]
    embedVar = discord.Embed(title="Ween Leaderboard Locator", description="Ween is in: " + str(leaderloc) + " place. Let's go [WEEN] squad!", color=discord.Color.blue())
    embedVar.set_image(url=IMG_URL)
    await ctx.send("", embed=embedVar, ephemeral=True)

        
    


async def setup(bot):
    bot.add_command(weenboard)
