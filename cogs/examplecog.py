from discord.ext import commands
import os
import discord
from data import db
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

class examplecog(commands.Cog):
    def __init__(self,bot):
        super().__init__()
        self.bot = bot
        self.db = db.getDB()

    @commands.Cog.listener()
    async def on_message(self, message):
        #don't bother if it's the bot
        if message.author.id == self.bot.application_id:
            return
        posts = 1
      
        cursor = self.db.cursor()
        try:
            cursor.execute(db.PICK_USER_POINTS+str(message.author.id))
            posts = cursor.fetchone()[0]
            posts = int(posts) + 1

            print(posts)
            val = (posts, message.author.id)
            command = "UPDATE users SET postcount = %s WHERE discordid=%s"
            cursor.execute(command, val)
            self.db.commit()

        except:
            user = (posts, int(message.author.id), message.author.name)
            cursor.execute(db.INSERT_USER, user)
            self.db.commit()
            print("record inserted")

async def setup(bot):
    await bot.add_cog(examplecog(bot=bot))