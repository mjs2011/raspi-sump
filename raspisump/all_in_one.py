# -*- coding: utf-8 -*-

# This code originally written with Spyder in Windows. Code then moved to pi. 
# It is called from csv_rename.py. 
# The intent of this file is to consolidate individual days worth of CSV data
# into a single master csv file, so there are no gaps in data across files.
# the script looks at master.csv to determine how many days need to be added
# to the file.  
# once master.csv is created, the data can be analyzed to determine when pump
# cycles occur. This is where the inefficiencies start. These pump cycles, or 
# inflections, are recalculated every time all_in_one.py is run, rather than 
# the inflection data also being stored in the csv file to be added to as 
# needed. This means that while only new csv files are being read each day, 
# pump cycle time is being recaluclated for all 90 days, each time this script
# is called. 
# Once inflections are found, cycle times are calculated and stored in matrix.
# this matrix is then graphed, and the cycle time graph is stored as a png to 
# be shown on the webserver home page. 

#code needs cleanup and likely needs major programming changes for efficiency.

#Max Sauer - 8/31/2021

"""
Spyder Editor

This is a temporary script file.
"""

import csv
import glob
import time
#import codecs
#import shutil
import numpy as np
import matplotlib as mpl

mpl.use("Agg")

import matplotlib.dates as mdates
import matplotlib.pyplot as plt

#need to import config parser to read info from raspisump.conf
import configparser

def time_plot():
    path = r'/home/pi/raspi-sump/charts/csv'
    file_name = (path + "/" + "master.csv")
    allFiles = sorted(glob.glob(path + "/*.csv"))
    #allFiles = glob.glob(path + "/*.csv")
    #daysToGrab = 10
    
    config = configparser.RawConfigParser()
    
    config.read('/home/pi/raspi-sump/raspisump.conf')

    configs = {'days': config.getint('cycle_time', 'days'),
               'time': config.getint('cycle_time', 'time')
               }

    daysToGrab = configs['days']
    height = configs['time']
    
    print('days to grab is ')
    print(daysToGrab)
    print('ylim is ')
    print(height)
    
    try:
        #with open(file_name, 'wb') as outfile:
        with open(file_name, mode='r') as outfile:
            reader = csv.reader(outfile, delimiter = ",")
            first = []
            last = []
            data = []
            for row in reader:
                data.append(row)
            first = data[0]
            first = first[0]
            first = first[:10]
            last = data[-1]
            last = last[0]
            last = last[:10]
            print("file opened \n")
        outfile.close()
    except:
        print("error opening file, it will be created")
        len_files = len(allFiles)
        if len_files < daysToGrab:
            allFiles_new = allFiles[:-1]
        else:
            allFiles_new = allFiles[-daysToGrab:-1]
        length_files = len(allFiles_new)
        date_from_file = []
        #new_name = []
        
        for k in range(length_files):
            temp = allFiles_new[k]
            temp = temp[-12:]
            temp = temp[:8]
            temp = temp[:4] + "-" + temp[4:6] + "-" + temp[6:] + " "
            date_from_file.append(temp)
	
#added print command for troubleshooting
            print(date_from_file[k])
            
            with open(allFiles_new[k], mode = 'r') as f:
                reader = csv.reader(f, delimiter = ",")
                data = []
                for row in reader:
                    data.append(row)
            f.close()
                    
            time = []
            value = []
            date_time = []
            
            length = len(data)
            for i in range(length):
                temp = data[i]
                time_ = temp[0]
                value_ = temp[1]
                time.append(time_)
                value.append(value_)
                
            for i in range(length):
                date_new_ = date_from_file[k] + time[i]
                date_time.append(date_new_)
            csvData = [date_time, value]
            
            #'w' means write (python3), 'a' means append, so add on to the csv instead of overwrite
            with open(file_name, 'a', newline='') as outfile:
                #shutil.copyfileobj(csvData,outfile)
                writer = csv.writer(outfile)
                writer.writerows(list(zip(*csvData)))
                print(file_name + ' opened')
            outfile.close()
                
        with open(file_name, mode='r') as outfile:
            reader = csv.reader(outfile, delimiter = ",")
            first = []
            last = []
            data = []
            for row in reader:
                data.append(row)
            first = data[0]
            first = first[0]
            first = first[:10]
            last = data[-1]
            last = last[0]
            last = last[:10]
            print("file opened \n")
        outfile.close()
    finally:
        print(first)
        print(last)
        print('from master.csv before finally')
        
        length_files = len(allFiles)
        print(length_files)
        date_from_file = []
        #new_name = []
        
        for k in range(length_files):
            temp = allFiles[k]
            temp = temp[-12:]
            temp = temp[:8]
            temp = temp[:4] + "-" + temp[4:6] + "-" + temp[6:]
            date_from_file.append(temp)
            
        for i in range(length_files):
            if last == date_from_file[i]:
                grab_ = i
                print('i is ')
                print(i)
    
        #print(allFiles)
        allFiles_new = allFiles[grab_+1:-1]
        print(' ')
        print(allFiles_new)
        length_files = len(allFiles_new)
        date_from_file = []
        
        for k in range(length_files):
            print('k is ')
            print(k)
            temp = allFiles_new[k]
            temp = temp[-12:]
            temp = temp[:8]
            temp = temp[:4] + "-" + temp[4:6] + "-" + temp[6:] + " "
            date_from_file.append(temp)
            
            with open(allFiles_new[k], mode = 'r') as f:
                reader = csv.reader(f, delimiter = ",")
                data = []
                for row in reader:
                    data.append(row)
            f.close()
            
            time = []
            value = []
            date_time = []
            
            length = len(data)
            for i in range(length):
                temp = data[i]
                time_ = temp[0]
                value_ = temp[1]
                time.append(time_)
                value.append(value_)
                
            for i in range(length):
                date_new_ = date_from_file[k] + time[i]
                date_time.append(date_new_)
            csvData = [date_time, value]
            
            #'w' means write (python3), 'a' means append, so add on to the csv instead of overwrite
            with open(file_name, 'a', newline='') as outfile:
                #shutil.copyfileobj(csvData,outfile)
                writer = csv.writer(outfile)
                writer.writerows(list(zip(*csvData)))
                print(file_name + ' opened')
            outfile.close()
       
    #Load all contents of Master CSV File         
        date, value = np.loadtxt(file_name, delimiter=',', unpack=True, 
                                     converters={0: lambda x: mdates.datestr2num(x.decode('utf8'))})
        with open(file_name) as f:
            list2 = [row.split()[0] for row in f]
        
    #create new array of files to find location to start plotting at, based on daysToPlot
        length_files = len(allFiles)
        temp = []
        for k in range(length_files):
            temp = allFiles[k]
            temp = temp[-12:]
            temp = temp[:8]
            temp = temp[:4] + "-" + temp[4:6] + "-" + temp[6:]
            date_from_file.append(temp)
        
        len_files = len(date_from_file)
        if len_files < daysToGrab:
            start_date = date_from_file[0]
        else:
            start_date = date_from_file[-daysToGrab]
    
    #find the location in the date list that contains the start date we are looking for   
        length = len(list2)
        for i in range(length):
             if start_date == list2[i]:
                grab_new = i
                break
        else:
            grab_new = 0

        print('start date location is ')
        print(grab_new)
            
    #trim down the date and value arrays from master csv to only data we want to plot based on daysToPlot         
        date = date[grab_new:]
        value = value[grab_new:]
    
        length = len(value)
        delta_t = []
        delta_h = []
        inflection = []
     
    #find where the pump cycled and store in inflect, along with cycle time in delta_t
        for i in range(length-1):
            delta = (date[i+1]-date[i])*86400
            delta_t.append(delta)
            delta = value[i+1]-value[i]
            if delta < -1:
                inflect = 1
            else:
                inflect = 0
            inflection.append(inflect)
    
            
    #calculate summed time between inflection points (pump cycles)
        time_sum = [60]
    #    print(length)
    #    print(len(inflection))
        for i in range(length-2):
           # print(i)
            if inflection[i] == 0:
                time = delta_t[i+1]+time_sum[i]
                time_sum.append(time)
            else:
                time = 0
                time_sum.append(time)
               
    #calculate cyle time based on time sum
        cycle_time = []
        for i in range(length-2):
            if time_sum[i+1] == 0:
                cycle = time_sum[i]/60
                cycle_time.append(cycle)
            else:
                cycle = 0
                cycle_time.append(cycle)
                
    #create matrix of data for easier viewing
        matrix = np.column_stack((date[1:], delta_t, inflection, time_sum))
        
        xs = np.array(date[2:])
        ys = np.array(cycle_time)
        zs = np.array(value[2:])
        
        ax1 = plt
        ax1.title('Sump Pump Cycle Time')
        ax1.xlabel('Time')
        ax1.ylabel('cycle time (min)')
        ax1.plot_date(xs, ys, 'k-')
        hfmt = mdates.DateFormatter('%m-%d %H:%M')
        ax1.ylim(0,height)
        plt.gcf().autofmt_xdate()
        ax1.grid()
                
        plot_name = (path + "/" + "cycle_time.png")
        plt.savefig(plot_name, dpi = 200)
        
        print('cycle_time.png saved successfully')
