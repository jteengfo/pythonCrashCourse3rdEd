from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv

path = Path('chapter16\san_francisco (16.3)\san_francisco_weather_2021.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_column = next(reader)

# initialize variable/s
station_name = ''

# find which index DATE, TMAX, TMIN, STATION is 
date_index = header_column.index('DATE')
tmin_index = header_column.index('TMIN')
tmax_index = header_column.index('TMAX')
station_index = header_column.index('STATION')

# print(date_index, tmin_index, tmax_index)

for index, column in enumerate(header_column):
    print(index, column)

# extract information -- DATE, TMAX, TMIN

dates, highs, lows = [], [], []

for row in reader:
    try:
        date = datetime.strptime(row[date_index], '%Y-%m-%d')
        high = int(row[tmax_index])
        low = int(row[tmin_index])
    except ValueError:
        print("Missing data in %s", date)
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

    if not station_name:
        station_name = row[station_index]


# visualize data using matplotlib

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.3)
ax.plot(dates, lows, color='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, alpha=0.1)

# format graph
ax.set_title(f"High & Low Air Temperature in {station_name} 2021", fontsize=24)
plt.ylim(0, 100)
fig.autofmt_xdate
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', labelsize=16)

plt.show()
