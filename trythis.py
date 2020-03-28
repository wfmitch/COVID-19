import os
import sys
from datetime import datetime
import dateparser
import logging
import csv
import numpy as np
import matplotlib.pyplot as plt
import math
logging.basicConfig(filename='trythis.log',filemode='w',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
logging.info("Program Started")

with open('csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_confirmed_global.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    dates = next(reader)
    totals = np.zeros(len(dates)-1) 
    log_totals = np.zeros(len(dates)-1)
    logging.info(dates[len(dates)-1])
    for row in reader:
        if row[1] == 'US':
            for days in range(4,len(dates)-1):
                totals[days] = totals[days] + int(row[days])
for days in range(4,len(dates)-1):
    log_totals[days] = math.log(totals[days]) 
for days in range(4,len(dates)-1):
    true_dates[days] = dateparser.parse(dates[days])   
plt.figure()
plt.suptitle('US Confirmed Cases vs Log of Confirmed Cases')
plt.xlabel('time (days)')
plt.ylabel('Cases')
plt.subplot(211)
plt.title('Confirmed Cases')
plt.plot(dates[4:len(dates)-1],totals[4:len(dates)])
plt.subplot(212)
plt.title('Log of Confirmed Cases')
plt.plot(dates[4:len(dates)-1],log_totals[4:len(dates)])


plt.show()
logging.info("Program Finished")