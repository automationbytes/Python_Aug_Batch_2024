# import datetime
# print(datetime.datetime.now())

'''
ref:

https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

'''
from datetime import datetime as dt

currenttime = dt.now()
print(currenttime)

#current day
print(currenttime.strftime("%a")) #Sat
print(currenttime.strftime("%A")) #Saturday

#date
print(currenttime.strftime("%d")) #24

#month
print(currenttime.strftime("%b")) #Aug
print(currenttime.strftime("%B")) #August

print(currenttime.strftime("%m")) #08

#year
print(currenttime.strftime("%y")) #24
print(currenttime.strftime("%Y")) #2024

#hours
print(currenttime.strftime("%H")) #0-24 #21

print(currenttime.strftime("%I %p")) #0-12

#mins
print(currenttime.strftime("%M")) #00-60

#seconds
print(currenttime.strftime("%S")) #00-60

print(currenttime.strftime("%x")) #date
print(currenttime.strftime("%X")) #time
print(currenttime.strftime("%c")) #Sat Aug 24 21:05:01 2024

#timezone
print(currenttime.strftime("%Z"))

