# MR_MALIBUS


#About
MR_Malibus is a bot that I am writing for the GamingW discord.
Feel free to do whatever with this code.



#Configuration

#Dependencies
loadenv for loading the environment variables
Discord.py

#Create configuration file:
Put the following in a .env file:
```
DISCORD_TOKEN={Discord bot token}
WEATHER_KEY=0 to disable or put your OpenWeatherAPI key here
```

#Modules:

|  Module | Description   |
| ------------ | ------------ |
|  addquote  | Adds a quote to a data.json file in the working directory of the bot.    |
|  quote   | Pulls a quote from the data.json at random.  |
|  example  | This is a test command. You can use this as a blueprint to create new commands. Replace test in the source file with the name of the command you wish to make. |
| weather |  Uses openweather api to give you a rudimentary weather forecast. Usage: !weather cityname |



