import os
import sys
import datetime
import dateparser
import logging
import csv
import numpy as np
import matplotlib.pyplot as plt
import math


t1 = ['Jun 1 2005  1:33PM','Aug 28 1999 12:00AM']
dt1 = []
print(t1)

for i in t1: 
    dt1 = dateparser.parse(i)

print(dt1)