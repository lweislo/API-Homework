# Unit 6 | Assignment - What's the Weather Like?

## Background

This assignment asked to use various Python libraries, Matplotlib and Pandas to determine how weather changes with latitude, eg. does it really get warmer the closer one gets to the equator?

![Equator](Images/equatorsign.png)

## Weather.Py

#### Dependencies:

* matplotlib.pyplot, pandas, numpy, requests, time, sys, urllib, openweathermapy, time, seaborn, scipy
* api_key from api_keys
* citipy from citipy

The included weather.py script contains several functions used in the analysis:

* city_data() - takes no parameters. This will create a random array of latitude and longitude values, pass them to Citipy and return a total number of valid cities collected. It will pass that list of cities to the city_sets() function.
* city_sets(cities - list of strings) - takes one parameter, a list of city names. This function breaks up the original set into chunks that should bypass the OpenWeatherMapy API's limit of 60 calls/minute. It returns both the number of sets created and the actual list of ranges for evaluation, and prompts the user to continue if satisfied. If OK'd, it will pass the list of cities and the sets on to the owm_api() function.
* owm_api(cities - list of strings, sets - list of lists of pairs of whole numbers) - accepts parameters cities, sets - these are expected to be lists of cities (strings) and sets (list of lists of pairs of whole numbers). WARNING: This function requires a valid API key in api_keys.py, in the same folder as the script.
    ** The outputs will be a logfile in the log folder - the filename will be './log/log_(current timestamp).txt'
    ** owm_api passes the parsed data and the timestamp output file name (./data/out_(current timestamp).csv) to the weather_df function
* weather_df(data, filename) - accepts the parsed data and output location from owm_api, then stores the data as the output csv filename.

## Running the weather analysis:

The .csv file created by the above functions can then be analysed by running weather_analysis(filename). This puts the data into a current dataframe that can safely be subjected to numerous plots or manipulations without altering the original dataset. 




