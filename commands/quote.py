import random
import json
import discord
from discord.ext import commands
from data import quotes
quotesdata = [quotes.Quotes("test", "test"), quotes.Quotes("test2", "test2")]
@commands.command()
async def quote(ctx):
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
    quotesdata = [quotes.Quotes(item['author'],item['quote']) for item in data]
    randquote = random.choice(quotesdata)
    embedVar = discord.Embed(title="A quote by: "+randquote.author, description=randquote.quote, color=discord.Color.blue())
    
    await ctx.send("", embed=embedVar, ephemeral=True)

async def setup(bot):
    bot.add_command(quote)
