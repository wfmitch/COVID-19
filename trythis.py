import os
import sys
from datetime import datetime
import logging
import csv
import matplotlib.pyplot as plt

logging.basicConfig(filename='trythis.log',filemode='w',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
RC = 0
logging.info("Program Started")
with open('.\\archived_data\\archived_time_series\\time_series_19-covid-Confirmed_archived_0325.csv', newline='') as csvfile:
     reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    #  for row in reader:
    #      plt.plot(reader)
plt.plot([1, 2, 3, 4])
plt.ylabel('some numbers')
plt.show()
logging.info("Program Finished")
exit(RC)