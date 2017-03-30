from pandas import *
from ggplot import *
from datetime import datetime

def plot_weather_data(turnstile_weather):
    '''
    You are passed in a dataframe called turnstile_weather. 
    Use turnstile_weather along with ggplot to make a data visualization
    focused on the MTA and weather data we used in assignment #3.  
    You should feel free to implement something that we discussed in class 
    (e.g., scatterplots, line plots, or histograms) or attempt to implement
    something more advanced if you'd like.  

    Here are some suggestions for things to investigate and illustrate:
     * Ridership by time of day or day of week
     * How ridership varies based on Subway station (UNIT)
     * Which stations have more exits or entries at different times of day
       (You can use UNIT as a proxy for subway station.)

    If you'd like to learn more about ggplot and its capabilities, take
    a look at the documentation at:
    https://pypi.python.org/pypi/ggplot/
     
    You can check out:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv
     
    To see all the columns and data points included in the turnstile_weather 
    dataframe. 
     
    However, due to the limitation of our Amazon EC2 server, we are giving you a random
    subset, about 1/3 of the actual data in the turnstile_weather dataframe.
    '''

    # Ridership by time of the day
    ridership_time = ggplot(turnstile_weather, aes(x = 'Hour', y = 'ENTRIESn_hourly')) \
                   + geom_point(alpha = 0.25, color = 'navy') \
                   + xlab('Time of the day') + ylab('Number of passengers') \
                   + scale_x_discrete(breaks = [1, 5, 9, 13, 17, 21], \
                                      labels = ['01:00', '05:00', '09:00', '13:00', '17:00', '21:00'])
    #print ridership_time

    # Ridership by day of the week
    turnstile_weather['DATEn'] = to_datetime(turnstile_weather['DATEn'])
    turnstile_weather['DAYn'] = turnstile_weather['DATEn'].apply(lambda x: x.strftime('%w'))
    ridership_day = ggplot(turnstile_weather, aes(x = 'DAYn', y = 'ENTRIESn_hourly')) \
                  + geom_point(alpha = 0.25, color = 'maroon') \
                  + xlab('Day of the week') + ylab('Number of passengers') \
                  + scale_x_discrete(breaks = range(7), \
                                     labels = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI'])
    #print ridership_day

    # Ridership by station
    turnstile_weather['UNIT'] = turnstile_weather['UNIT'].apply(lambda x: int(x[1:]))
    ridership_station = ggplot(turnstile_weather, aes(x = 'UNIT', y = 'ENTRIESn_hourly')) \
                      + geom_point(alpha = 0.25, color = 'black') \
                      + xlab('Station') + ylab('Number of passengers')
    #print ridership_station

    # Average ridership per day over time for UNIT 001
    q = """SELECT DATEn, AVG(meantempi) FROM turnstile_weather GROUP BY """
    return [ridership_time, ridership_day, ridership_station]

turnstile_weather_file = open('turnstile_data_master_with_weather.csv', 'r')
turnstile_df = read_csv(turnstile_weather_file)
print plot_weather_data(turnstile_df)