from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

path = Path("chapter16\sitka_rainfall (16.1)\sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_column = next(reader)

for index, column in enumerate(header_column):
    print(index, column)

# Extract information we want -- PRCP, Date 
dates, prcps = [], []
for row in reader:
    try:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        prcp = row[5]
    except ValueError:
        print(f"Missing data for {date}")
    else:   
        dates.append(date)
        prcps.append(prcp)

# Visualize data 
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, prcps, color='blue', linewidth=1)

# Format plot 
ax.set_title("Daily Precipitation Levels in Sitka, 2021")
fig.autofmt_xdate
ax.set_ylabel("PRCP")
ax.tick_params(axis="both", labelsize=16)
ax.yaxis.set_major_locator(plt.MaxNLocator(20))

plt.show()
