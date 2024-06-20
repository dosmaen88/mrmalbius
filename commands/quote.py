import random
import json
import discord
from discord.ext import commands
quotes = ["Quotes haven't been loaded yet, oops."]
@commands.command()
async def quote(ctx):
    f = open('data.json')
    quotes = json.load(f)

    embedVar = discord.Embed(title="Random quote:", description=random.choice(quotes), color=discord.Color.blue())
    
    await ctx.send("", embed=embedVar, ephemeral=True)

async def setup(bot):
    bot.add_command(quote)
