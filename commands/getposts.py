from discord.ext import commands
import os
import discord
from data import db
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

scores = [10,20,30,40,50,60]
titles = ["cool","wicked", "spiffy", "fantastic", "tubular", "splendid"]


def getpostsresponse(posts):
    i = 0
    for score in scores:
        title = titles[i]
        if score > posts:
            return title
        i = i + 1 
        
    

@commands.command()
async def getposts(ctx, name):
    sqldb = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"), 
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
    )
    cursor = sqldb.cursor()
    print(cursor)
    print(db.PICK_NAME_POINTS+name)
    cursor.execute(db.PICK_NAME_POINTS+"'"+name+"'")
    posts = cursor.fetchone()
    if posts:
        await ctx.send(name + " has: " +str(posts[0])+" posts. They are: " + getpostsresponse(posts[0]))
        return
    await ctx.send("Couldn't find a user by that name!")
    

async def setup(bot):
    bot.add_command(getposts)
