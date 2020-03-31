"""Graph sump pit activity."""

# Raspi-sump, a sump pump monitoring system.
# Al Audet
# http://www.linuxnorth.org/raspi-sump/
#
# All configuration changes should be done in raspisump.conf
# MIT License -- http://www.linuxnorth.org/raspi-sump/license.html

import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style
from matplotlib import dates

import time
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

try:
    import ConfigParser as configparser  # Python2
except ImportError:
    import configparser  # Python3

config = configparser.RawConfigParser()
config.read("/home/pi/raspi-sump/raspisump.conf")
configs = {"unit": config.get("pit", "unit")}

try:
    configs["line_color"] = config.get("charts", "line_color")
except configparser.NoSectionError:
    configs["line_color"] = "FB921D"


MPL_VERSION = int(mpl.__version__.split(".")[0])  # Matplotlib major version


def graph(csv_file, filename):
    """Create a line graph from a two column csv file."""

    df = pd.read_csv(csv_file)
    df.columns  = ['time', 'reading']
    df['time'] = pd.to_datetime(df['time'],format='%H:%M:%S')

    plt.savefig(filename, dpi=72)
    style.use('seaborn-poster')

    plt.rcParams['axes.facecolor']='ffffff'
    plt.rcParams['grid.color']='ECE5DE'

    fig = plt.figure(figsize=(12, 3.5))
ax = fig.add_subplot(111)
fig.set_facecolor('w')

plt.plot_date(
        df.time,
        df.reading,
        ls="solid",
        linewidth=2,
        color="#000000",
        fmt='-'
        )
title = "Sump Pit Water Level {}".format(time.strftime("%Y-%m-%d %H:%M"))
title_set = plt.title(title)
title_set.set_y(1.09)

  
#hfmt = dates.DateFormatter('%H:%M')
hfmt = dates.DateFormatter('%I:%M %p')
cwl = 10
plt.axhline(cwl, color='#007f7f', label="Critical Level", linewidth=2)
plt.ylabel("inches")

plt.xlabel("Time of Day")
ax.xaxis.set_major_formatter(hfmt)

plt.xticks(rotation=30) 
plt.legend()

plt.savefig(filename, dpi=72)