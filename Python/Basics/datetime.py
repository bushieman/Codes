import datetime

x = datetime.datetime.now() 
print(x)# display the current date
print(x.year)# display the year

# use strftime to convert datetime object to string
print(x.strftime('%a'))# weekday, short version i.e fri
print(x.strftime('%A'))# weekday, full version i.e friday
print(x.strftime('%w'))# weekday, number version i.e 5
print(x.strftime('%d'))# Day of month i.e 01-31	31	
print(x.strftime('%b'))# Month name, short version i.e Dec	
print(x.strftime('%B'))# Month name, full version ie. December	
print(x.strftime('%m'))# Month as a number 01-12 i.e 12	
print(x.strftime('%y'))# Year, short version, without century i.e 18	
print(x.strftime('%Y'))# Year, full version	i.e 2018	
print(x.strftime('%H'))# Hour 00-23 i.e 17	
print(x.strftime('%I'))# Hour 00-12 i.e 05	
print(x.strftime('%p'))# AM/PM i.e PM	
print(x.strftime('%M'))# Minute 00-59 i.e 41	
print(x.strftime('%S'))# Second 00-59 i.e 08	
print(x.strftime('%f'))# Microsecond 000000-999999 i.e 548513	
print(x.strftime('%z'))# UTC offset i.e +0100	
print(x.strftime('%Z'))# Timezone i.e CST	
print(x.strftime('%j'))# Day number of year 001-366 i.e 365	
print(x.strftime('%U'))# Week number of year, Sunday as the first day of week, 00-53 i.e 52	
print(x.strftime('%W'))# Week number of year, Monday as the first day of week, 00-53 i.e 52	
print(x.strftime('%c'))# Local version of date and time i.e Mon Dec 31 17:41:00 2018	
print(x.strftime('%C'))# Century i.e 20	
print(x.strftime('%x'))# Local version of date i.e 12/31/18	
print(x.strftime('%X'))# Local version of time i.e 17:41:00	
print(x.strftime('%%')) # A % character i.e %	
print(x.strftime('%G')) # ISO 8601 year i.e 2018	
print(x.strftime('%u')) # ISO 8601 weekday (1-7) i.e 1	
print(x.strftime('%V')) # ISO 8601 weeknumber (01-53) i.e 01

# create a datetime obj
x = datetime.datetime(2020, 5, 17)
print(x) 

# use strptime to convert string to datetime object
datetime_str = '2018-06-29 08:15:27.243860'
datetime_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')
print(datetime_obj, type(datetime_obj))
