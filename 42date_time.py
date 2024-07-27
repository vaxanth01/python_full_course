import datetime as dt

today = dt.datetime.today()
print(today)


new = dt.date(2023,10,12)
print(new)
print(new.year)
print(new.month)
print(new.day)

a=dt.date(2025,6,23)
print(a)
b=dt.date.today()
print(b)
c=a-b
print(c)

