"""
usage:
$ python plot_latency.py <logfile>
$ python plot_latency.py log170829.txt
"""
import matplotlib.pyplot as plt
import pandas as pd
import sys
plt.rcParams['font.size'] = 20

names = ['date', 'time', 'raspi', 'latency', 'unit']
df = pd.read_csv(sys.argv[1], sep=' ', names = names)
bins = df['latency'].max()*1000
fig = plt.figure(figsize=(10,10))

for raspi_name, data in df.groupby('raspi'):
    print(data['latency'].value_counts())
    plt.clf()
    plt.hist(data['latency']*1000, bins=int(bins), range=(0, bins))
    plt.xlabel('latency[ms]')
    plt.ylabel('counts')
    plt.title('histgram_' + str(raspi_name))
    fig.savefig('hist_' + str(raspi_name) + '.png')
