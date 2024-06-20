from discord.ext import commands
from types import SimpleNamespace
import json
from data import quotes
quotesdata = [quotes.Quotes("test", "test"), quotes.Quotes("test2", "test2")]
@commands.command()
@commands.has_permissions(administrator=True)
async def addquote(ctx, author, quote):
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
    quoteslist = [quotes.Quotes(item['author'],item['quote']) for item in data]

    if len(quotesdata) >= 999:
        await ctx.send("There are too many quotes")
        return
    
    quoteslist.append(quotes.Quotes(author, quote))

    with open('data.json', 'w', encoding='utf-8') as x:
        json.dump(quoteslist, x, ensure_ascii=False, indent =4, cls=quotes.QuotesEncoder)
    await ctx.send("Quote added")

async def setup(bot):
    with open("data.json", "r") as json_file:
        data = json.load(json_file)
    quoteslist = [quotes.Quotes(item['author'],item['quote']) for item in data]
    bot.add_command(addquote)
