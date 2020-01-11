import datetime

'''
datetime.time(hours, minutes, seconds)
'''

# creates new instance of time
# https://docs.python.org/2/library/datetime.html#time-objects
t = datetime.time(5,10,15)

print(t) # 05:10:15

print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)


'''
dates
datetime.date
'''

# get today
today = datetime.date.today()

print(today)

print(today.timetuple()) # tuple that provides all the time information for the specific date
