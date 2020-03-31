import os
import sys
import datetime
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
    totals = np.zeros(len(dates)) 
    log_totals = np.zeros(len(dates))
    base_date = dateparser.parse(dates[4])
    true_dates = [base_date + datetime.timedelta(days=x) for x in range(len(dates)-4)]
    for row in reader:
        if row[1] == 'US':
            for days in range(4,len(dates)):
                totals[days] = totals[days] + int(row[days])
for days in range(4,len(dates)):
    log_totals[days] = math.log(totals[days])
plt.figure()
plt.suptitle('US Confirmed Cases vs Log of Confirmed Cases')
plt.xlabel('time (days)')
plt.ylabel('Cases')
plt.subplot(211)
plt.title('Confirmed Cases')
plt.plot(dates[4:len(dates)],totals[4:len(dates)])
plt.subplot(212)
plt.title('Log of Confirmed Cases')
plt.plot(dates[4:len(dates)],log_totals[4:len(dates)])
plt.show()
logging.info("Program Finished")