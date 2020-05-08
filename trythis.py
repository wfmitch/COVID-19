import os,sys,dotenv,logging,dateparser,random,argparse,pathlib2,csv,requests,math 
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from _datetime import timedelta

if __name__ == '__main__':
    logging.basicConfig(filename='trythis.log',filemode='w',format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',level=logging.DEBUG)
    logging.info("Program Started")
    response = requests.get('https://api.covid19data.cloud/')
    response.json()
    with open('csse_covid_19_data\\csse_covid_19_time_series\\time_series_covid19_confirmed_global.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        dates = next(reader)
        totals = np.zeros(len(dates)-4) 
        log_totals = np.zeros(len(dates)-4)
        base_date = dateparser.parse(dates[4])
        true_dates = [base_date + timedelta(days=x) for x in range(len(dates)-4)]
        for row in reader:
            if row[1] == 'US':
                for days in range(4,len(dates)):
                    totals[days-4] = totals[days-4] + int(row[days])
    for days in range(4,len(dates)):
        log_totals[days-4] = math.log(totals[days-4])
    plt.figure()
    plt.suptitle('US Confirmed Cases vs Log of Confirmed Cases')
    plt.xlabel('time (days)')
    plt.ylabel('Cases')
    plt.subplot(211)
    plt.title('Confirmed Cases')
    plt.plot(true_dates,totals)
    plt.subplot(212)
    plt.title('Log of Confirmed Cases')
    plt.plot(true_dates,log_totals)
    plt.show()
    logging.info("Program Finished")