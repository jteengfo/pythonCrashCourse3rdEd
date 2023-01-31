from pathlib import Path
import matplotlib.pyplot as plt 
from datetime import datetime
import csv

path_sitka = Path('chapter16\sitka-death_valley_comparison (16.2)\sitka_weather_2021_full.csv')
path_valley = Path('chapter16\sitka-death_valley_comparison (16.2)\death_valley_2021_full.csv')

lines_sitka = path_sitka.read_text().splitlines()
lines_valley = path_valley.read_text().splitlines()

reader_sitka = csv.reader(lines_sitka)
header_column_sitka = next(reader_sitka)

reader_valley = csv.reader(lines_valley)
header_column_valley = next(reader_valley)

print("Sitka: ")
for index, column in enumerate(header_column_sitka):
    print(index, column)
print("\n Death-Valley: ")
for index, column in enumerate(header_column_valley):
    print(index, column)


# extract information for both sitka and valley

dates_sitka, highs_sitka, lows_sitka = [], [], []
dates_valley, highs_valley, lows_valley = [], [], []

for row in reader_sitka:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[7])
        low = int(row[8])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates_sitka.append(current_date)
        highs_sitka.append(high)
        lows_sitka.append(low)

for row in reader_valley:
    try:
        date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[6])
        low = int(row[7])
    except ValueError:
        print(f"Missing data for {date}")
    else:
        dates_valley.append(date)
        highs_valley.append(high)
        lows_valley.append(low)
        

# visualize data
plt.style.use('classic')
fig, ax = plt.subplots()
# sitka
ax.plot(dates_sitka,highs_sitka, color='blue', linewidth=1, alpha=0.3)
ax.plot(dates_valley,lows_sitka,color='red', linewidth=1, alpha=0.3)
plt.fill_between(dates_sitka, highs_sitka, lows_sitka, color='blue', alpha=0.1)
# death valley
ax.plot(dates_valley, highs_valley, color='blue', linewidth=1, alpha=0.3)
ax.plot(dates_valley, lows_valley, color='red', linewidth=1, alpha=0.3)
plt.fill_between(dates_valley, highs_valley, lows_valley, color='red', alpha=0.1)


# format plot 
title = "Comparison of high and low temperatures between Sitka and Death Valley for 2021"
ax.set_title(title, fontsize=20)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)")
ax.yaxis.set_major_locator(plt.MaxNLocator(10))
plt.tick_params(axis="both", labelsize=16)
# plt.ylim(0, 1)
plt.show()