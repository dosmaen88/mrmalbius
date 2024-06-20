from discord.ext import commands
from dotenv import load_dotenv
import os
import requests, json

load_dotenv()

base_url="http://api.openweathermap.org/data/2.5/weather?"
api_key = os.getenv("WEATHER_KEY")


@commands.command()
async def weather(ctx, *, cityname: str):
    if (api_key == "0"):
        print("no api key found, will not function")
        return
    complete_url = base_url + "appid=" + api_key + "&q=" + cityname + "&units=imperial"
    print(complete_url)
    response = requests.get(complete_url)
    print("request sent")

    jdata = response.json()
    print("test")
    if jdata["cod"] != "404":
            print ("Bot is typing")
            y = jdata["main"]

            current_temperature = str(y["temp"])
        
            _msg = "The temperature in " + cityname + " is: " + str(current_temperature)
            await ctx.send(_msg)
    else: 
        await ctx.send("Weather info could not be found for: " + cityname)

    
    
    
   

async def setup(bot):
    bot.add_command(weather)
