import requests
from plyer import notification
import time

API_KEY = ""
CITY = 'Dallas'

def get_weather():
    url = f'http://api.weatherstack.com/current?access_key={API_KEY}&query={CITY}'
    response = requests.get(url)
    data = response.json()
    return data

def show_notification(weather_data):
    weather = weather_data['current']
    temperature = weather['temperature']
    description = weather['weather_descriptions'][0]

    notification_title = f'Weather in {CITY}'
    notification_message = f'{description}, Temperature: {temperature}°C'

    notification.notify(
        title=notification_title,
        message=notification_message,
        app_name='Weather Notification',
        timeout=10  # Notification will be shown for 10 seconds
    )

if __name__ == 'show_notification(weather_data)':
    while True:
        weather_data = get_weather()
        show_notification(weather_data)
        time.sleep(3600)  # Fetch and show notification every hour