#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get high temperatures from file.
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs = [], []
    for row in reader:
        high = int(row[1])
        highs.append(high)
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
    print(highs)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# Setting the format.
plt.title("Daily high remperatures, July 2014", fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=14)
plt.tick_params('both', which='major', labelsize=16)
plt.show()