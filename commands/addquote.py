from discord.ext import commands
import json
quotes = ["sample quotes go here", "beautiful words and fluffy things"]
@commands.command()
async def addquote(ctx, *, quote):
    f = open('data.json')
    quotes = json.load(f)
    if len(quotes) >= 999:
        await ctx.send("There are too many quotes")
        return
    quotes.append(quote)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(quotes, f, ensure_ascii=False, indent =4)
    await ctx.send("Quote added")

async def setup(bot):
    f = open('data.json')
    quotes = json.load(f)
    bot.add_command(addquote)
