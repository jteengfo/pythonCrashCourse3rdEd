from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv

path = Path('chapter16\san_francisco (16.3)\san_francisco_weather_2021.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_column = next(reader)

for index, column in enumerate(header_column):
    print(index, column)

# extract information -- DATE, TMAX, TMIN

dates, highs, lows = [], [], []

for row in reader:
    try:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print("Missing data in %s", date)
    else:
        dates.append(date)
        highs.append(high)
        lows.append(low)

# visualize data using matplotlib

plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.3)
ax.plot(dates, lows, color='blue', alpha=0.3)
plt.fill_between(dates, highs, lows, alpha=0.1)

# format graph
ax.set_title("High & Low Air Temperature in San Francisco 2021", fontsize=24)
plt.ylim(0, 100)
fig.autofmt_xdate
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', labelsize=16)

plt.show()
