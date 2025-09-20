# 🌤️ Haki Weather Discord Bot

A simple Discord bot that provides **current weather information** for any location using the **OpenWeatherMap API**.  
Users can request weather by typing commands in the format:

```
haki.[location]
```

---

## 🚀 Features
- Retrieve **temperature, feels like, min & max temperature** in Celsius.
- Handles **invalid locations** gracefully with an error message.
- Displays weather info in **Discord embed messages** for better readability.
- Customizable command prefix.

---

## 🛠️ Tech Stack
- **Python 3.8+**
- [discord.py](https://discordpy.readthedocs.io/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- `requests` for HTTP requests
- `json` for parsing API responses

---

## 📂 Project Structure
```
.
├── main.py        # Discord bot main file
├── weather.py     # Helper functions for parsing weather data and embeds
└── README.md      # Project documentation
```

---

## ⚡ Setup Instructions

### 1️⃣ Prerequisites
- Python 3.8 or higher
- A Discord account and server for testing
- A [Discord bot token](https://discord.com/developers/applications)
- An [OpenWeatherMap API key](https://openweathermap.org/api)

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/haki-weather-bot.git
cd haki-weather-bot
```

### 3️⃣ Install Dependencies
```bash
pip install discord.py requests
```

---

## ⚙️ Configuration

Update `main.py` with your credentials:

```python
token = "YOUR_DISCORD_BOT_TOKEN"
api_key = "YOUR_OPENWEATHERMAP_API_KEY"
command_prefix = 'haki.'
```

- `token`: Your Discord bot token  
- `api_key`: Your OpenWeatherMap API key  
- `command_prefix`: Prefix users will type to request weather (default: `haki.`)

---

## ▶️ Running the Bot

```bash
python main.py
```

- The bot will go online and set its activity to show the command prefix.
- Example usage in Discord chat:

```
haki.london
haki.toronto
```

---

## 🧩 How It Works

1. **User sends a message** starting with the command prefix.  
2. **Bot extracts the location** from the message.  
3. **Bot queries OpenWeatherMap API** for current weather data.  
4. **Bot parses the data** using `parse_data()` in `weather.py`.  
5. **Bot sends an embedded message** with temperature, feels like, min, and max.  
6. If location is invalid, the bot sends an **error embed**.

---

## 📌 Key Functions

**main.py**
- `on_ready()`: Sets bot presence and confirms the bot is online.  
- `on_message()`: Handles user commands and sends weather embeds.  

**weather.py**
- `parse_data(data)`: Filters relevant weather fields from the API response.  
- `weather_message(data, location)`: Creates a Discord embed for valid weather info.  
- `error_message(location)`: Creates a Discord embed for invalid location errors.
