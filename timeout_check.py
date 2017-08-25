import pandas as pd
import sys

names = ['date', 'time', 'raspi', 'latency', 'unit']
df = pd.read_csv(sys.argv[1], sep=' ', names = names)
df = df.dropna()

time_list = list(df['time'].unique())
raspi_list = list(df['raspi'].unique())

print('num. of timeout:')
for name in raspi_list:
    raspi_time_list = list(df[df['raspi'].isin([name])]['time'])
    timeout_list = list(set(time_list)-set(raspi_time_list))
    print(name, len(timeout_list))

print()
print('RPI at timeout:')
for time in time_list:
    time_raspi_list = df[df['time'].isin([time])]['raspi']
    raspiout_list = list(set(raspi_list) - set(time_raspi_list))
    if raspiout_list != []:
        print(time, raspiout_list)
