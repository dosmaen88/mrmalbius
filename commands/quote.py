import random
import json
from discord.ext import commands
quotes = ["Quotes haven't been loaded yet, oops."]
@commands.command()
async def quote(ctx):
    f = open('data.json')
    quotes = json.load(f)
    await ctx.send(random.choice(quotes))

async def setup(bot):
    bot.add_command(quote)
