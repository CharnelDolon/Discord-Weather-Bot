import discord

color = 0xFF6500
key_features = {
    'temp' : 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' : 'Minimum Temperature',
    'temp_max' : 'Maximum Temperature'
}

def parse_data(data):
    data = data['main']
    del data['pressure']
    del data['humidity']
    return data

def weather_message(data, location):
    location = location.title()
    message = discord.Embed(
        title = f'{location} Weather (Celsius)',
        description = f'Here is the weather in {location}.',
        color = color
    )

    for key in key_features:
        message.add_field(
            name = key_features[key],
            value = str(data[key]),
            inline = False
        )
    return message

def error_message(location):
    location = location.title()
    return discord.Embed(
        title='Error',
        description=f'There was an error retrieving weather data for {location}.',
        color=color
    )
    