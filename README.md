# Surf's Up - SQL Alchemy Challenge
This project analyzes temperature and preciptation data captured between 2010 and 2017 to help with trip planning to Honolulu, Hawaii. In addition to data exploration and visualization, a simple app is developed to return data based on static and dynamic endpoints.

## Python Libraries
* matplotlib
* numpy
* pandas
* datetime
* sqlalchemy
* scipy
* flask

## Datasets
* [hawaii_measurements.csv][def1]
* [hawaii_stations.csv][def2]
* [hawaii.sqlite][def3]

## Analysis
### Part 1: Climate Analysis and Exploration
In this section, Python, Pandas, Matplotlib and SQL Alchemy are used to perform basic climate analysis and data exploration of a climate database.

#### Preciptation Analysis
This chart shows precipitation measurements from each station during the latest 12 months of data (Aug 2016-Aug 2017). The minimum, average, and maximum rainfall during this time was 0.00", 0.18", and 6.70" from 2021 observations.

![Daily Precipitation by Day][def4]

![Preciptation Statistics][def5]

#### Station Analysis
There are a total of 9 stations with climate records in this dataset. The most active station from 2010-2017 was USC00519281, with 2772 daily records. The minimum, average, and maximum precipation for this station was 0.00", 0.21", and 9.64".

The temperature measurements at the most active station during the latest 12 months (Aug 2016-Aug 2017) are skewed left, peaking in the mid 70s.

![Temps in Hawaii][def6]

### Part 2: Create Endpoints for Climate App
This app is developed using Flask, Pandas, Datetime, and SQL Alchemy to return query results based on precipitation, temperature, and station data in the csv files.

#### Endpoints
* `/` - Lists all available routes
* `/api/v1.0/precipitation` - Returns precipitation values by date
* `/api/v1.0/stations` - Returns a list of stations
* `/api/v1.0/tobs` - Returns temperature observations by date for the most active station during the last year of data (Aug 2016-Aug 2017).
* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>` - Returns the minimum, average, and maximum temperatures for the specified date range. The start and end dates should be entered in in YYYY-MM-DD format.

### Other Analyses
#### Is there a meaningful difference between the temperatures in June and December in Hawaii?
The average temperature in Hawaii is 74.9F in June versus 71.0F in December. This difference in temperature is statistically significant (unpaired t-test pvalue = 4.19e-187).

#### What were normal historic temperatures and rainfall in Hawaii between August 1-7?
The minimum, average, and maximum temperatures between Aug 1-7 from 2010-2017 were 72.0F, 79.2F, and 83.0F.

![Trip Avg Temp][def7]

Normal temperatures during this time of the year are represented in the chart below:

![Normal temperatures][def8]

[def1]: Resources/hawaii_measurements.csv
[def2]: Resources/hawaii_stations.csv
[def3]: Resources/hawaii.sqlite
[def4]: Images/precipitation.png
[def5]: Images/describe.png
[def6]: Images/station-histogram.png
[def7]: Images/temperature.png
[def8]: Images/daily-normals.png