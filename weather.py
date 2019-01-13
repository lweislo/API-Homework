# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import sys
import urllib
import openweathermapy as owm
from time import sleep
import seaborn as sbn
from scipy import stats

# Import API key
from config import api_key
import warnings
warnings.filterwarnings('ignore')
# Incorporated citipy to determine city based on latitude and longitude
from citipy import citipy


# city_list() <---Comment this out until you want to run it


#For offline analysis, go back to the original csv file
def weather_analysis(filename):
    print(f'Getting a dataframe from the file {filename}...')
    try:
        weather_data = pd.read_csv(filename, encoding='UTF-8', index_col=0, parse_dates=True, infer_datetime_format=True)
        weather_data['Daytime'] = ''
        weather_data.set_index('City', drop=True)
        for i in range(0,len(weather_data)):
            if (weather_data.iloc[i,6] - weather_data.iloc[i,8]) >= 0 and (weather_data.iloc[i,6] - weather_data.iloc[i,9]) < 0:
                weather_data.iloc[i,12] = 'Day'
            else:
                weather_data.iloc[i,12] = 'Night'
        return weather_data
    except FileNotFoundError:
        print("File not found.")

# Need to find out how to get line breaks to work
def w_stats(col1, col2):
    slope, intercept, r_value, p_value, std_err = stats.linregress(col1, col2)
    s_stats = f'Slope: {slope}. Intercept: {intercept}. R: {r_value}. P: {p_value}. SE: {std_err}'
    return s_stats

# Create a function to generate a dataframe, then CSV copy of the dataframe

def weather_df(data, filename):
    try:
        column_names = ["City","Humidity", "Min Temp","Max Temp","Wind Speed","Cloudiness","Date","Country","Sunrise","Sunset","Lat","Lon"]
        weather_data = pd.DataFrame(data, columns=column_names)
        weather_data.set_index('City')
        weather_data.to_csv(filename, encoding='UTF-8', header=True)

        print(f'Your data are now available here: {filename}.')
        print(f'To get this data in a DataFrame, use weather_analysis(filename).')
    except FileNotFoundError:
        print("File not found.")

# Function to do the API calls
def owm_api(cities, sets):

    weather_data = []
    # Create a settings object with the API key and preferred units
    settings = {'units': 'metric', 'appid': api_key}
    # Create a list of parameters to keep
    summary = ['name','main.humidity', 'main.temp_min','main.temp_max','wind.speed','clouds.all' ,'dt','sys.country', 'sys.sunrise','sys.sunset','coord.lat', 'coord.lon']

    # Work with the log file to record the API calls/errors
    timestr = time.strftime('%Y%m%d-%H%M%S')
    log = './log/log_' + timestr + '.txt'
    output = './data/out_' + timestr + '.csv'
    print(f'Your data will be in {output} and all calls will be logged in {log}')

    with open(log, 'a+') as f:

        for n in range(0, len(sets)):
            # Generate a list of cities for each subset range
            sub_cities = cities[sets[n][0]:sets[n][1]]

            for city in sub_cities:
                status = (f'Getting data for set number {n}: {city}... ')
                f.write(status)
                print(status)
                #Perform the API call on OWM
                try:
                    city_data = owm.get_current(city, **settings)
                    weather_data.append(city_data)
                #Log the result
                    msg = 'Success!\n'
                    f.write(msg)
                    print(msg)

                except urllib.error.HTTPError:
                    msg = 'City not found\n'
                    f.write(msg)
                    print(msg)
                except NameError:
                    msg = 'API key not valid\n'
                    f.write(msg)
                    print(msg)

    data = [response(*summary) for response in weather_data]
    weather_df(data, output)

# Function to break up the list of cities into sets

def city_sets(cities):
    arr = np.arange(0, len(cities), round(len(cities)/12))
    arr= np.append(arr,len(cities))
    sets = []
    for i in range(len(arr)-1):
        sets.append([arr[i], arr[i+1]])
    print(f'Breaking up the list of cities into {len(sets)} sets for processing.')
    print(f'{sets}')
    choice = input("Do you wish to proceed with the download? (Y/N): ")
    choice = choice.upper()
    if "Y" not in choice:
        print("Quitting! Goodbye")
        sys.exit()
    else:
        owm_api(cities, sets)

# Function to make a list of random coordinates and pick the nearest city
def city_list():
    # Range of latitudes and longitudes
    lat_range = (-90, 90)
    lng_range = (-180, 180)
    # List for holding lat_lngs and cities
    cities = []
    lat_lngs = []
    # Create a set of random lat and lng combinations
    lats = np.random.uniform(low=-90.000, high=90.000, size=1500)
    lngs = np.random.uniform(low=-180.000, high=180.000, size=1500)

    lat_lngs = zip(lats, lngs)
    # Identify nearest city for each lat, lng combination
    for lat_lng in lat_lngs:
        city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name

        # If the city is unique, then add it to a our cities list
        if city not in cities:
            cities.append(city)
    print(f'The random array of coordinates resulted in a list of {len(cities)} valid cities.')
    city_sets(cities)
