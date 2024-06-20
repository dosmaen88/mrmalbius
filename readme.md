MR_Malibus is a bot that I am writing for the GamingW discord.
Feel free to do whatever with this code.
test

Prequisites:
loadenv for loading the environment variables
Discord.py

Put the following in a .env file:
DISCORD_TOKEN={Discord bot token}
WEATHER_KEY=0 to disable or put your OpenWeatherAPI key here

Modules:

Addquote:
Adds a quote to a data.json file

Quote:
Grabs a random quote from a data.json file

Example:
This is a test module, you can copy/paste this and build your own modules off of it. Replace test in async def test(ctx) and test in bot.add_command(test) with the name of your command, and replace the function with your own functionality.

Weather:
!weather [[cityname]]
A simple weather forcasting module. Uses the OpenWeather API.




