from discord.ext import commands

@commands.command()
async def slap(ctx, *, targname: str):
    
    msg = str(ctx.author) + " slapped " + targname + " with a large trout."
    await ctx.send(msg)

async def setup(bot):
    bot.add_command(slap)
