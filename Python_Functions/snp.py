from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import pandas.io.data as web
from numpy import random 

def random_num(N):
    gen = random.random(N)
    for x in range(0,len(gen)):
        pos = random.random(1)
        if pos < 0.4:
            gen[x] = -1 * gen[x]
    return gen

def random_unif(N):
    gen = random.uniform(-.0999,.1,N)
    return gen

def Monte(N):
    mont = random_unif(N)
    mont[0]=0
    for x in range(1, len(mont)):
        mont[x] = 100*mont[x] + mont[x-1]
        if mont[x] < 0:
            mont[x] = mont[x] *-1
    return mont

def Average_Monte(N,m):
    avg = []
    for x in range(0,m):
        mont = Monte(N)
        for s in range(0,len(mont)):
            avg[s] = avg[s] + mont[s]
    relavg = [i / m for i in avg]
    return relavg

data = web.get_data_yahoo('^GSPC', '1950-01-01')['Adj Close']
data_rets = data.pct_change()

N = len(data)

fig = plt.figure()
fig.suptitle('S&P 500 Adjusted Closing Price and Percent Change', fontsize = 14, fontweight='bold')
fig.subplots_adjust(left=None, bottom=0.1, right=None, top=0.9, wspace=0.2, hspace=0.7)

ax1 = fig.add_subplot(311)
ax1 = data.plot()
ax1.set_title('Closing Price vs Date')
ax1.set_xlabel('Date')
ax1.set_ylabel('Adj Close')

ax2 = fig.add_subplot(312)
data_rets.plot()
ax2.set_title('Percent Change vs Date')
ax2.set_xlabel('Date')
ax2.set_ylabel('Percent Change')

ax3 = fig.add_subplot(313)
ax3 = plt.plot(range(N),Monte(N),range(N),Monte(N),range(N),Monte(N))
#ax3 = plt.plot(range(N),Average_Monte(N,10))
plt.title('Monte Carlo Estimate')
plt.xlabel('Date')
plt.ylabel('Closing Price')




plt.show()
