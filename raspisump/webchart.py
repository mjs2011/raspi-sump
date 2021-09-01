'''Create charts for viewing on Raspberry Pi Web Server.'''

# Raspi-sump, a sump pump monitoring system.
# Al Audet
# http://www.linuxnorth.org/raspi-sump/
#
# All configuration changes should be done in raspisump.conf
# MIT License -- http://www.linuxnorth.org/raspi-sump/license.htmlimport os

import os
import subprocess
import time
from raspisump import todaychart
from datetime import date, timedelta

def create_folders(year, month, homedir):
    '''Check if folders exist in charts folder and create them if they don't'''
    if not os.path.isdir('{}charts/{}/'.format(homedir, year)):
        _year = 'mkdir {}charts/{}'.format(homedir, year)
        create_year = _year.split(' ')
        subprocess.call(create_year)

    if not os.path.isdir('{}charts/{}/{}/'.format(homedir, year, month)):
        _month = 'mkdir {}charts/{}/{}'.format(homedir, year, month)
        create_month = _month.split(' ')
        subprocess.call(create_month)


def create_chart(homedir):
    '''Create a chart of sump pit activity and save to web folder'''
    csv_file = '{}charts/csv/waterlevel-{}.csv'.format(
        homedir, time.strftime('%Y%m%d')
        )
    filename = '{}charts/today.png'.format(homedir)
    bytes2str = todaychart.bytesdate2str('%H:%M:%S')
    todaychart.graph(csv_file, filename, bytes2str)


def copy_chart(year, month, today, homedir):
    '''Copy today.png to year/month/day folder for web viewing'''
    copy_cmd = 'cp {}charts/today.png {}charts/{}/{}/{}.png'.format(
        homedir, homedir, year, month, today
        )
    copy_file = copy_cmd.split(' ')
    subprocess.call(copy_file)

    yesterday = date.today() - timedelta(1)
    yesterday_day = yesterday.strftime('%d')
    yesterday = date.today() - timedelta(1)
    yesterday_day = yesterday.strftime('%d')
    yesterday_copy_cmd = 'cp {}charts/{}/{}/{}{}{}.png {}charts/yesterday.png'.format(homedir, year, month, year, month, yesterday_day, homedir
      )
    yesterday_copy_file = yesterday_copy_cmd.split(' ')
    subprocess.call(yesterday_copy_file)

    dbf = date.today() - timedelta(2)
    dbf_day = dbf.strftime('%d')
    dbf_copy_cmd = 'cp {}charts/{}/{}/{}{}{}.png {}charts/dbf.png'.format(
      homedir, year, month, year, month, dbf_day, homedir
      )
    dbf_copy_file = dbf_copy_cmd.split(' ')
    subprocess.call(dbf_copy_file)


    dbf2 = date.today() - timedelta(3)
    dbf2_day = dbf2.strftime('%d')
    dbf2_copy_cmd = 'cp {}charts/{}/{}/{}{}{}.png {}charts/dbf2.png'.format(
      homedir, year, month, year, month, dbf2_day, homedir
      )
    dbf2_copy_file = dbf2_copy_cmd.split(' ')
    subprocess.call(dbf2_copy_file)
