#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle
import numpy as np
import pandas as pd

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

df = pd.DataFrame.from_dict(enron_data).transpose()
print "Number of rows:", df.shape[0]
print "Number of cols:", df.shape[1]
print "Number of POIs:", np.count_nonzero(df['poi'])
print "Total stock of James Prentice:", df.loc['PRENTICE JAMES', 'total_stock_value']
print "No emails to POIs from Wesley Colwell:", df.loc['COLWELL WESLEY', 'from_this_person_to_poi']
print "Stock options exercised by Jeff Skilling:", df.loc['SKILLING JEFFREY K', 'exercised_stock_options']
# with pd.option_context('display.max_rows', None, 'display.max_columns', 3):
#     print df.iloc[:,1]
# exit()
print "Total payments of Jeff Skilling:", df.loc['SKILLING JEFFREY K', 'total_payments']
print "Total payments of Kenneth Lay:", df.loc['LAY KENNETH L', 'total_payments']
print "Total payments of Andrew Fastow:", df.loc['FASTOW ANDREW S', 'total_payments']
print "Number of non-NaN salaries:", len(df['salary'].unique())
print "Number of known email addresses:", len(df['email_address']) - df['email_address'].value_counts()['NaN']
print "Percentage of people with unknown payments:", df['total_payments'].value_counts()['NaN'] * 1.0 / len(df)
print "Number of POIs with unknown payments:", df['total_payments'][df['poi'] == True].isnull().sum()
# print df.describe()
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):
#     print df.iloc[1, :  ]


