#Tianna Hatch
# 2/25/2022

import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textfield.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "ENTER YOUR OWN API HERE" 
    #enter your own API above 
    
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']

    temp = int(json_data['main']['temp'])
    temp = 1.8*(temp-273) + 32 #convert to fahrenheit
    mintemp = int(json_data['main']['temp_min'])
    mintemp = 1.8*(mintemp-273) + 32 #convert to fahrenheit
    maxtemp = int(json_data['main']['temp_max'])
    maxtemp = 1.8*(maxtemp-273) + 32 #convert to fahrenheit

    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    #convert sunrise / sunset to 12 hour format and adjust for EST timezone (-5 hours or 18000 seconds)
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 18000))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 18000))

    final_info = condition + "\n" + str(temp) + "°F"
    final_data = "\n" + "Max Temp: " + str(maxtemp) + "°F" + "\n" + "Min Temp: " + str(mintemp) + "°F" + "\n" + "Pressure: " +str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset 

    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("390x600")
canvas.title("Python Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textfield = tk.Entry(canvas, font = t)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font = t)
label1.pack()
label2 = tk.Label(canvas, font = f)
label2.pack()

canvas.mainloop()
