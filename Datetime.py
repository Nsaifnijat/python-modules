# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 10:06:55 2021

@author: Hamdard PC
"""

#different ways to extract time form date time

import datetime as dt
from datetime import timezone

'''
# 1- extracting time from time module, getting PC time and timezone
import time
current_time=time.strftime('%H:%M:%S')
print(current_time)'''

# 2-extracting time from datetime module

# to UTC timezone, using datetime timezone
current_date_time=dt.datetime.now(tz=timezone.utc)
time_of_datetime=current_date_time.strftime("%H:%M:%S")
print(time_of_datetime)

#to PC timezone
times=dt.datetime.now()
print(times.strftime("%H:%M:%S"))


#to create date, dont use, 2016,04,24 it gives syntax error
d=dt.date(2016, 4, 24)
print(d)
# current date
tday=dt.date.today()
print(tday)
#getting the year
print(tday.year) 
print(tday.day)
#getting weekday two ways
print(tday.weekday()) # Monday= 0, sunday=6
print(tday.isoweekday()) #Monday=1, sunday=7

#adding and subtracting date with timedelta
tdelta=dt.timedelta(days=7)
print(tday+tdelta)
print(tday-tdelta)
#if we add or subtract date and timedelat we get date, date1+timedelta=date
# but date1+date2=timedelta

#lets find how many days left to my birthday
bday=dt.date(2021, 11, 5)
till_bday=bday-tday
print(till_bday)
#few methods on timedelta
#only days or all in seconds
print(till_bday.days)
print(till_bday.total_seconds())

#creating time, time(hour,minute,second,millisecond)
t=dt.time(10,20,4,233333)
print(t)
print(t.minute)
print(t.second)


#date and time combined

dtime=dt.datetime(2018, 8, 23,5,23,54,11111)
print(dtime)
#methods
print(dtime.date())
print(dtime.time())
print(dtime.year)
print(dtime.hour)

#add and subtract
tddelta=dt.timedelta(days=7)
print(dtime+tddelta)
tddelta=dt.timedelta(hours=3)
print(dtime-tddelta)

#using alternative constructors which come with  datetime

dt_today=dt.datetime.today() # current local datetime with no timezone, it does not take timezone as parameter
dt_now=dt.datetime.now() # current local datetime if tz=none, otherwise it get to that tz
dt_utcnow=dt.datetime.utcnow() #current utcnow but tz is none

print(dt_today)
print(dt_now)
print(dt_utcnow)

#event though datetime has a timezone class but for better flexibility and better usage pytz is recommende. pip install pytz
import pytz
somedate=dt.datetime(2019, 2, 24, 8,9,23, tzinfo=pytz.UTC)
print(somedate)
#Todays date time in UTC
utc_now=dt.datetime.now(tz=pytz.UTC)
cur_day=dt.datetime.utcnow().replace(tzinfo=pytz.UTC)#you can put whatever timezone
print(utc_now)
print(cur_day)

# to get the timezones in the pytz
for tz in pytz.all_timezones:
    print(tz)


#changing utc timezone to my own timezone, intelligent datetime
utc_now=dt.datetime.now(tz=pytz.UTC)
print(utc_now)

#to kabul time
kabultime=utc_now.astimezone(pytz.timezone('Asia/Kabul'))
print(kabultime)



#changing naive datetime to different timezones if the following does not work, use step two
dt_now_kabul=dt.datetime.now()
dt_eastern=dt_now_kabul.astimezone(pytz.timezone('US/Eastern'))
print(dt_now_kabul)
print(dt_eastern)

#method two
dt_now_kabul=dt.datetime.now()
dt_kabul_tz=pytz.timezone('Asia/Kabul')
dt_now_kabul=dt_kabul_tz.localize(dt_now_kabul)
dt_eastern2=dt_now_kabul.astimezone(pytz.timezone('US/Eastern'))
print(dt_eastern2)

#working with the two useful methods
dt_now_kabul=dt.datetime.now(tz=pytz.timezone('US/Eastern'))
print(dt_now_kabul.strftime('%B %d, %Y'))


#note strptime in format you pass the format that the date is in
dts='October 08, 2021'
dt_convert=dt.datetime.strptime(dts, '%B %d, %Y')
print(dt_convert)


print((datetime.datetime.now()-datetime.timedelta(minutes=50)))


from datetime import date
from datetime import datetime
today = date.today()
midnight = datetime.combine(today, datetime.min.time())
print(today)
print(midnight)
print('Midnight: %s ' % (midnight) )

print(datetime.min.time())


now = datetime.now()

forma = now.strftime('%H:%M')
forma = "15:43"
nex = "15:44"
if forma > nex:
    print('yes')
print(forma)










