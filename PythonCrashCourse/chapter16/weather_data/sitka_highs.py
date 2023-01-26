from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt


path = Path('chapter16\weather_data\sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column in enumerate(header_row):
    print(index, column)

# want to extract high temperatures -- know that its in pos 4 
dates, highs, lows = [], [], []
for row in reader: 
    date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4]) # because its a str otherwise
    low = int(row[5])
    dates.append(date)
    highs.append(high)
    lows.append(low)
print(highs)

# visualize data using matplotlib
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')
ax.fill_between(dates, highs, lows, alpha=0.1)

# format plot 
ax.set_title("Daily High & Low Temperatures, 2021")
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperature', fontsize=16)
ax.tick_params(labelsize=16)
fig.autofmt_xdate()

plt.show()

