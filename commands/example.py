from discord.ext import commands

@commands.command()
async def test(ctx):
    await ctx.send("This is a test command. If you can see this, then the bot is working!")

async def setup(bot):
    bot.add_command(test)
