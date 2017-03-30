from pandas import *
import pandasql
from ggplot import *
from datetime import datetime

def avg_rides_per_day(filename):
    turnstile_weather = pandas.read_csv(filename)
    turnstile_weather.rename(columns = lambda x: x.lower(), inplace = True)

    q = """
    SELECT
    daten, avg(entriesn_hourly)
    FROM
    turnstile_weather
    GROUP BY
    daten
    """
    
    #Execute your SQL command against the pandas frame
    avg_daily_rides = pandasql.sqldf(q.lower(), locals())
    return avg_daily_rides

def plot_results(df):
	df['daten'] = to_datetime(df['daten'])
	gg = ggplot(df, aes(x = 'daten', y = 'avg(entriesn_hourly)')) \
	   + geom_point() \
	   + geom_line() \
	   + xlab('Day of the month') + ylab('Number of rides') \
	   + scale_x_date(breaks = date_breaks('7 days'), labels = '%m/%d/%Y')
	print gg

turnstile_weather_file = open('turnstile_data_master_with_weather.csv', 'r')
avg_daily_rides = avg_rides_per_day(turnstile_weather_file)
plot_results(avg_daily_rides)
