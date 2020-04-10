import os,sys,dotenv,logging,dateparser,random,argparse,json,pprint
from datetime import date
from datetime import timedelta

import csv
import requests
import numpy as np
import matplotlib.pyplot as plt
import math

if __name__ == '__main__':
    logging.basicConfig(filename='trythis.log',filemode='w',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
    logging.info("Program Started")
    last_date = date.today()
    start_date = last_date - timedelta(1)
    logging.info(last_date) 
    logging.info(start_date)       

    r = requests.get('https://api.covid19data.cloud/v1/jh/daily-reports/?last_update_from='+str(start_date)+'&last_update_to='+str(last_date)+'&country=US')
    logging.info(r)
    if r.status_code != 200:
        sys.exit(422)
    count = 0
    total_deaths = 0
    total_confirmed = 0
    total_recovered = 0
    for d in r.json():
        total_deaths = total_deaths + d["deaths"]
        total_confirmed = total_confirmed + d["confirmed"]
        total_recovered = total_recovered + d["recovered"]
        count = count + 1
    print(r.json())
    print(count,total_confirmed,total_deaths,total_recovered)
    

    #  dates = next(reader)
    #     totals = np.zeros(len(dates)-4) 
    #     log_totals = np.zeros(len(dates)-4)
    #     base_date = dateparser.parse(dates[4])
    #     true_dates = [base_date + timedelta(days=x) for x in range(len(dates)-4)]
    #     for row in reader:
    #         if row[1] == 'US':
    #             for days in range(4,len(dates)):
    #                 totals[days-4] = totals[days-4] + int(row[days])
    # for days in range(4,len(dates)):
    #     log_totals[days-4] = math.log(totals[days-4])
    # plt.figure()
    # plt.suptitle('US Confirmed Cases vs Log of Confirmed Cases')
    # plt.xlabel('time (days)')
    # plt.ylabel('Cases')
    # plt.subplot(211)
    # plt.title('Confirmed Cases')
    # plt.plot(true_dates,totals)
    # plt.subplot(212)
    # plt.title('Log of Confirmed Cases')
    # plt.plot(true_dates,log_totals)
    # plt.show()
    logging.info("Program Finished")