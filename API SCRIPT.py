import requests
import matplotlib.pyplot as plt
from datetime import datetime

# my actual OpenWeatherMap API key
API_KEY = 'dae7a296b8f641a560f2ad675f906271'
#Allow user to input city name via terminal 
CITY = 'india'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetched weather data from OpenWeatherMap
response = requests.get(URL)
data = response.json()

# Check if response was successful
if response.status_code != 200:
    print(f"Failed to retrieve data: {data.get('message', 'Unknown error')}")
    exit()

# Extract datetime and temperature
dates = []
temperatures = []

for entry in data['list']:
    date = datetime.strptime(entry['dt_txt'], "%Y-%m-%d %H:%M:%S")
    temp = entry['main']['temp']
    dates.append(date)
    temperatures.append(temp)

# Plotting
plt.figure(figsize=(15, 8))
plt.plot(dates, temperatures, marker='o', linestyle='-', color='teal')
plt.title(f'5-Day Temperature Forecast for {CITY}')
plt.xlabel('Date & Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
