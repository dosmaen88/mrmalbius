from discord.ext import commands
import os
import discord
from data import db
import mysql.connector
from dotenv import load_dotenv
load_dotenv()

CREATE_USER_TABLE = "CREATE TABLE users (sqlid INT AUTO_INCREMENT PRIMARY KEY, postcount BIGINT, discordid BIGINT, name VARCHAR(32))"
INSERT_USER = "INSERT INTO users (postcount, discordid, name) VALUES (%s, %s, %s)"
PICK_USER_POINTS = """select postcount from users where discordid="""
PICK_NAME_POINTS = """select postcount from users where name="""
UPDATE_POINTS = "UPDATE users SET postcount = %s WHERE discordid=%s"
def getDB():
    db = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"), 
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
    )

    cursor = db.cursor()


    try:
        cursor.execute(CREATE_USER_TABLE)
    except:
        cursor.execute("SHOW TABLES")
    for x in cursor:
        print(cursor)
    return db
