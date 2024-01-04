import discord
import json
import requests
from weather import parse_data, weather_message, error_message

token = "myauthkey"
api_key = "myapikey"
command_prefix = 'haki.'

client= discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{command_prefix}[location]'))
    print('{0.user} BOT is ready'.format(client))
    
@client.event
async def on_message(message):
    if (message.author != client.user) and (message.content.startswith(command_prefix)):
        location = message.content.replace(command_prefix, '').lower()
        if len(location) >= 1:
            #Get weather data
            url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
            #&units=metric
            try:
                print("This is working")
                data = json.loads(requests.get(url).content)
                # Print data
                data = parse_data(data)
                print(data)
                print("This is working 2")
                json_str = json.dumps(data, indent=4)
                print(json_str)
                await message.channel.send(embed=weather_message(data, location))
            except KeyError: 
                await message.channel.send(embed=error_message(location))
                print(KeyError.message)
                
client.run(token)
