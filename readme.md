# MR_MALBIUS


About:

Mr_Malbius is a bot that I am writing for the GamingW discord using Python.
Feel free to do whatever with this code.



Configuration:
Please feel free to delete any of the files in the commands folder to remove an extension that you will not use.
I'm aware that weenboard is oddly specific but you could adjust the code there to look at other clans if you wanted.

Dependencies:\n
loadenv for loading the environment variables
Discord.py
mysql.connector

Create configuration file:
Put the following in a .env file:
```
DISCORD_TOKEN={Discord bot token}
WEATHER_KEY=0 to disable or put your OpenWeatherAPI key here
MYSQL_HOST=location of your MYSQL server
MYSQL_USER=username for mysql 
MYSQL_PASSWORD= password for mysql
MYSQL_DATABASE= the table name you want to use
```
There's a helper string in DB.py that you can use for a reference for building the expected table. 
CREATE_USER_TABLE = "CREATE TABLE users (sqlid INT AUTO_INCREMENT PRIMARY KEY, postcount BIGINT, discordid BIGINT, name VARCHAR(32))"

Modules:

|  Module | Description   |
| ------------ | ------------ |
|  addquote  | Adds a quote to a data.json file in the working directory of the bot.    |
|  quote   | Pulls a quote from the data.json at random.  |
|  example  | This is a test command. You can use this as a blueprint to create new commands. Replace test in the source file with the name of the command you wish to make. |
| weather |  Uses openweather api to give you a rudimentary weather forecast. Usage: !weather cityname |
| randomgame | pulls a random free game from itch.io |
| weenboard | Locates where my friend's Territorial.io clan is|
| ween | Displays a random hotdog themed image for my friend's discord server |
| getposts | Returns the amount of posts / messages a user has made, requires SQL |
| examplecog | an example background process that looks for messages, and then keeps track of how many messages a user has made. |



