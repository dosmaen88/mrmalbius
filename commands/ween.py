from discord.ext import commands
import os
import random
import discord
BASE_DIR = os.getcwd() + "/imgs/ween/"


@commands.command()
async def ween(ctx):
    _title = "Let's go [WEENS]!"
    _description = "Hot diggity dog!"
    print (BASE_DIR)
    files = os.listdir(BASE_DIR)
    print(BASE_DIR+files[0])
    randnum = random.randint(0,len(files)-1)
    dir = BASE_DIR+files[randnum]

    file = discord.File(dir)
    embedVar = discord.Embed(title=_title, description=_description, color=discord.Color.blue())
    await ctx.send("", embed=embedVar, ephemeral=True, file=file)

        
    


async def setup(bot):
    bot.add_command(ween)
