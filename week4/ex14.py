import datetime

from dateutil import tz

d1 = datetime.datetime(1989, 4, 23, hour=11,
                  tzinfo=tz.gettz("America/New_York"))

print(d1)

d2 = datetime.datetime(1989, 4, 24, hour=10,
                       tzinfo=tz.gettz("America/Chicago"))

print(d2)

print(d1.hour > d2.hour)
print(d1 > d2)

d2_new_york_time = d2.astimezone(tz.gettz("America/New_York"))
print(d2_new_york_time)