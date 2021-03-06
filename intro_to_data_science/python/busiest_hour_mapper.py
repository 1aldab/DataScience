import sys
import string
import logging

# from util import mapper_logfile
# logging.basicConfig(filename=mapper_logfile, format='%(message)s',
#                     level=logging.INFO, filemode='w')

def mapper():
    """
    In this exercise, for each turnstile unit, you will determine the date and time 
    (in the span of this data set) at which the most people entered through the unit.
    
    The input to the mapper will be the final Subway-MTA dataset, the same as
    in the previous exercise. You can check out the csv and its structure below:
    https://s3.amazonaws.com/content.udacity-data.com/courses/ud359/turnstile_data_master_with_weather.csv

    For each line, the mapper should return the UNIT, ENTRIESn_hourly, DATEn, and 
    TIMEn columns, separated by tabs. For example:
    'R001\t100000.0\t2011-05-01\t01:00:00'

    Since you are printing the output of your program, printing a debug 
    statement will interfere with the operation of the grader. Instead, 
    use the logging module, which we've configured to log to a file printed 
    when you click "Test Run". For example:
    logging.info("My debugging message")
    Note that, unlike print, logging.info will take only a single argument.
    So logging.info("my message") will work, but logging.info("my","message") will not.
    """

    infile = sys.stdin
    header = next(infile).strip().split(",")
    unit_id = header.index('UNIT')
    entr_id = header.index('ENTRIESn_hourly')
    date_id = header.index('DATEn')
    time_id = header.index('TIMEn')
    no_cols = len(header)
    for line in infile:
        record = line.strip().split(",")
        if len(record) < no_cols:
            continue
        unit, entr, date, time = record[unit_id], record[entr_id], record[date_id], record[time_id]
        print "{0}\t{1}\t{2}\t{3}".format(unit, entr, date, time)

mapper()
