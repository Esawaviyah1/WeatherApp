import os
import json
import requests
import time

#gets the weather data for API
def getweather():
    geturl = "https://api.tomorrow.io/v4/timelines"
    apikey = ''
    location = [32.7767, 96.7970]

     #takes API data and puts it into dictionary
    querystring = {
        "location": "32, 96",
        "fields": ["temperature", "cloudCover", "humidity"],
        "units": "imperial",
        "timesteps": "1d",
        "apikey": '1or9T8BtPzG6hj225grix85051qYZCl9'}

    response = requests.request("GET", geturl, params=querystring)
    t = response.json()['data']['timelines'][0]['intervals'][0]['values']['temperature']

    results = None
     #breaking down data in dictionary into seperate parts
    results = response.json()['data']['timelines'][0]['intervals']
    for daily_result in results:
        date = daily_result['startTime'][0:10]
        temp = round(daily_result['values']['temperature'])
        humidity = response.json()['data']['timelines'][0]['intervals'][0]['values']['humidity']

        #creating new objects to format
        newdate = date[5:10]
        newtemp = '{0:.2f}'.format(((temp *1.8) +32))

        #printing for code window so we can see the output
        print("On", newdate, "it will be", newtemp, "F", humidity)

        #result string is for notification output
        resultString = f"On {newdate} it will be \nTempeture: {newtemp} F. \nHumidity: {humidity}%"
        return resultString

results = getweather()
def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))

notify("Weather Notification", f"Hello Aviyah, Heres your weather update for today! {results}")
#timed notification - every hour
time.sleep(15)