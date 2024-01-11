# -*- coding: utf-8 -*-

#scatterplots
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

x=[5,6,3,4,7,9]
y=[9,8,7,1,2,5]
#you can put a list of colors in the color argument, and sizes too
colors=[6,5,7,3,7,8]
sizes=[435,567,898,234,123,676]

#s=size, c=color, marker=marker, edgecolor= edge color, linewidth, alph,cmap=it gives different colors the base color
#plt.scatter(x,y, s=100,c='blue',marker='x', edgecolors='red', linewidths=2, alpha=0.5)
plt.scatter(x,y,s=sizes,c=colors, edgecolors='red', cmap='Greens',linewidths=1, alpha=0.90)
#logscales, makes skews lesser and makes thme relative
plt.xscale('log')
plt.yscale('log')
cbar=plt.colorbar()
cbar.set_label('Satisfaction')

#add padding to the plot 
plt.tight_layout()
plt.show()



#plotting datetime in a plot
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

dates= [
        datetime(2019,5,14),
        datetime(2019,5, 15),
        datetime(2019,5,16),
        datetime(2019,5, 17),
        datetime(2019,5,18),
        
        ]

y=[0,1,3,4,9]

plt.plot_date(dates,y, linestyle='solid')

#to format date in skew manner, gcf=current plot
plt.gcf().autofmt_xdate()
#to format the date
date_format=mpl_dates.DateFormatter('%b, %d %Y')
#to set it as the date format
plt.gca().xaxis.set_major_formatter(date_format)
plt.tight_layout()
plt.show()



#to read date from a csv and plot it
data=pd.read_csv('data.csv')
#the date in the data is a string we need to change it to datetime
data['Date']=pd.to_datetime(data['Date'])
data.sort_values('Date',inplace=True)

price_date=data['Date']
price_close=data['Close']

plt.plot_date(price_date,price_close, linestyle='solid')
plt.gcf().autofmt_xdate()
plt.title('Bitcoin price')
plt.xlabel('Date')
plt.ylabel('closing price')
plt.show()



#to plot a live plot
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
plt.style.use('fivethirtyeight')

x_vals=[]
y_vals=[]
index=count()

def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0, 5))
    #to update the current plot not to stack over it use cla()
    plt.cla()
    plt.plot(x_vals, y_vals)
    
#interval is time in milliseconds
anim =FuncAnimation(plt.gcf(), animate, interval=1000)
anim.save(anim)
plt.tight_layout()
plt.show()

#current axis
plt.gca()
#current figure
plt.gcf()



subplots


import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

x=[5,6,3,4,7,9]
y=[9,8,7,1,2,5]
d=[10,4,7,6,2,6]
z=[3,5,6,8,2,9]

fig,ax=plt.subplots()
ax.plot(x,y, label='Python')
ax.plot(x,d, label='Jawa')

ax.legend()
ax.set_title('plots')
ax.set_xlabel('AGE')
ax.set_ylabel('life')

#add padding to the plot 
plt.tight_layout()
plt.show()


























