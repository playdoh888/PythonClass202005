import calendar

c = calendar.Calendar()
print(list(c.itermonthdates(2020, 2)))

dates = list(d for d in c.itermonthdates(2019, 2) if d.month == 2)

print(dates)
