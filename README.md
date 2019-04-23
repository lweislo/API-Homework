# Unit 6 | Assignment - What's the Weather Like?

See the web application version of this assignment -> https://lweislo.github.io/API-Weather/

## Background

This assignment asked to use various Python libraries, Matplotlib and Pandas to determine how weather changes with latitude, eg. does it really get warmer the closer one gets to the equator?

## Weather.Py

#### Dependencies:

* matplotlib.pyplot, pandas, numpy, requests, time, sys, urllib, openweathermapy, time, seaborn, scipy
* api_key from api_keys (Open Weather Map API Key)
* citipy from citipy

* weather.py script creates a random array of latitude and longitude values, passes them to Citipy and returns a total number of valid cities collected. It then passes that list of cities to the city_sets() function.
* city_sets(cities) - takes one parameter, a list of city names. This function breaks up the original set into chunks that should bypass the OpenWeatherMapy API's limit of 60 calls/minute.
* owm_api(cities, sets) - Calls the OWM API and gathers current weather data for each city in the sets of cities. It requires a valid OWM API key in api_keys.py, in the same folder as the script.
    ** The outputs will be a logfile in the log folder - the filename will be './log/log_(current timestamp).txt'
    ** owm_api passes the parsed data and the timestamp output file name (./data/out_(current timestamp).csv) to the weather_df function
* weather_df(data, filename) - accepts the parsed data and output location from owm_api, then stores the data as the output csv filename.

## Running the weather analysis:

The .csv file created by the above functions can then be analysed by running weather_analysis(filename). This puts the data into a current dataframe that can safely be subjected to numerous plots or manipulations without altering the original dataset. 

## Plotting the data

Matplotlib and Seaborn were used to visualize the weather data to test the hypothesis that weather changes with proximity to the equator. A web site using Bootstrap styles was created to display the visualizations.
