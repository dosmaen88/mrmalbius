from discord.ext import commands
import random
import requests
import xml.etree.ElementTree as ET
import discord
from data import game
MAX_PAGE = 155
BASE_URL = 'https://itch.io/games/free.xml?page='
games = []

@commands.command()
async def randomgame(ctx):
    names = []
    links = []
    imgs = []
    page = BASE_URL + str(random.randint(0,MAX_PAGE+1))
    list_from_itch = requests.get(page)
    xml_document = list_from_itch.content

    root = ET.fromstring(xml_document)
    
    count = len(root.findall('channel/item/title'))
    
    for gameTitle in root.findall('channel/item/title'):
        names.append(gameTitle.text)
    
    for gameLink in root.findall('channel/item/link'):
        links.append(gameLink.text)
    
    for gameImage in root.findall('channel/item/imageurl'):
        imgs.append(gameImage.text)
    
    for title, link, img in zip(names, links, imgs):
        games.append(game.Game(title, link, img))
    rg = random.randint(1, len(names))
    embedVar = discord.Embed(title=games[rg].name, description=games[rg].link, color=discord.Color.blue())
    embedVar.set_image(url=games[rg].img)
    await ctx.send("", embed=embedVar, ephemeral=True)

        
    


async def setup(bot):
    bot.add_command(randomgame)
