#weatherdata_app.py
#July 28, 2022
#Joseph Poha Sivongxay 
#CIS 245
#Draft of weather data program that asks for user zipcode or city and provide weather forecast data
#--------------------------------------------------
import json, pip._vendor.requests

#Welcome message
print ('Welcome to the weather forecast program! \n')

#Ask for user input for city or zipcode


#Functions

#Option to use program again for users
def redoFunction():
    redo = input('Would you like to view the forecast for another city? Yes or No? \n')
    if redo == 'Yes':
        findWeather()
    elif redo == 'yes':
        findWeather()
    elif redo == 'no':
        print('Thank you. Goodbye.')
    elif redo == 'No':
        print('Thank you. Goodbye.')
    else:
        print('The value you entered is not correct. \nPlease try again\n')
        redoFunction()

#Main function for forecast data
def findWeather():
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    appid = "6b655718d3736a01c9e037f74aeaf175"
    location = input("Input city or zip code for weather information: \n") #ask users for city or zip code

    url = f"{base_url}?q={location}&units=imperial&APPID={appid}"
    response = pip._vendor.requests.get(url)
    unformated_data = response.json()
    #Try block that catches KeyError for invalid city or zipcode inputs by users
    try:
        locationName = unformated_data["name"] #finds name of location from unformated data
    except KeyError:
        print()
        print("Input is invalid please try again")
        print()
        findWeather()
    print()
    print("Weather forecast for " + locationName + ": ")
    print()
    #Forecast data
    temp = unformated_data["main"]["temp"]
    tempmax = unformated_data["main"]["temp_max"]
    tempmin = unformated_data["main"]["temp_min"]
    pressure = unformated_data["main"]["pressure"]
    windspeed = unformated_data["wind"]["speed"]
    humidity = unformated_data["main"]["humidity"]
    #Printing information for user
    print(f"The current temperature is: {temp}\u00B0C \nwith temperatures as high as {tempmax}\u00B0C or as low as {tempmin}\u00B0C")
    print()
    print(f"Total pressure is: {pressure}hPa")
    print()
    print(f"Wind speed is: {windspeed}m/s")
    print()
    print(f"Humidity is: {humidity}%")
    print()

    redoFunction()


findWeather()

#print data for view
#print(unformated_data)
