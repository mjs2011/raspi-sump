#!/usr/bin/python3

# This script passes the current date to yesterdaychart.py to be run. 
# called from Cron.
# Max Sauer

import time
from raspisump import yesterdaychart


def main():
    '''Pass variables to yesterdaychart.py'''
    today = time.strftime('%Y%m%d')
    homedir = '/home/pi/raspi-sump/'
    yesterdaychart.copy_chart(today, homedir)

if __name__ == '__main__':
    main()

