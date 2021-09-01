'''Create previous charts for viewing on Raspberry Pi Web Server.'''

# This script copies a given date's cycle time graph and saves a copy.
# The name of the file changes based on how many days old the graph is for.
# These copies of the png files are then used to show the last 3 days of data
# on the webserver. Files yesterday.png, dbf.png, and dbf2.png are saved and 
# shown on the webserver. These files are overwritten each time 
# yesterdaychart.py is called, which is currently set up at once a day with 
# cron. 

# MAX Sauer

import os
import subprocess
import time
from raspisump import todaychart
from datetime import date, timedelta


def copy_chart(today, homedir):
    '''copy previous day charts and move them to charts directory for webserver'''    
    yesterday = date.today() - timedelta(1)
    yesterday_day = yesterday.strftime('%d')
    month = yesterday.strftime('%m')
    year = yesterday.strftime('%Y')
    yesterday_copy_cmd = 'cp {}charts/{}/{}/{}{}{}.png {}charts/yesterday.png'.format(
      homedir, year, month, year, month, yesterday_day, homedir
      )
    yesterday_copy_file = yesterday_copy_cmd.split(' ')
    subprocess.call(yesterday_copy_file)
  
    dbf = date.today() - timedelta(2)
    dbf_day = dbf.strftime('%d')
    month = dbf.strftime('%m')
    year = dbf.strftime('%Y')
    dbf_copy_cmd = 'cp {}charts/{}/{}/{}{}{}.png {}charts/dbf.png'.format(
      homedir, year, month, year, month, dbf_day, homedir
      )
    dbf_copy_file = dbf_copy_cmd.split(' ')
    subprocess.call(dbf_copy_file)


    dbf2 = date.today() - timedelta(3)
    dbf2_day = dbf2.strftime('%d')
    month = dbf2.strftime('%m')
    year = dbf2.strftime('%Y')
    dbf2_copy_cmd = 'cp {}charts/{}/{}/{}{}{}.png {}charts/dbf2.png'.format(
      homedir, year, month, year, month, dbf2_day, homedir
      )
    dbf2_copy_file = dbf2_copy_cmd.split(' ')
    subprocess.call(dbf2_copy_file)

