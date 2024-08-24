
from datetime import date, timedelta
def datewithOffdate(days):
    today = date.today()
    offsetdate = today+timedelta(days)
    return offsetdate

print(datewithOffdate(3))
print(datewithOffdate(-3))

def datewithOffdate(days, format = "%m/%d/%Y"):
    today = date.today()
    offsetdate = today+timedelta(days)
    return offsetdate.strftime(format)

print(datewithOffdate(3))
print(datewithOffdate(-3))


print(datewithOffdate(3,"%y-%m"))
print(datewithOffdate(-3,"%d-%m-%y"))

print(datewithOffdate(3,"%B %d, %Y"))

