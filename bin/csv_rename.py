#!/usr/bin/python3
#this script is called from cron, which then runs all_in_one.py

import time
#from raspisump import csv_renamer
#from raspisump import cycle_time_plot
from raspisump import all_in_one

def main():
   #run csv_file_list in csv-renamer.py
   #csv_renamer.csv_file_list()
   #cycle_time_plot.time_plot()
   all_in_one.time_plot()

if __name__ == '__main__':
    main()

