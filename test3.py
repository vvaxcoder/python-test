from datetime import datetime, timedelta
import locale

# today = date.today()
# print(today)
# print(today.day)
# print(today.month)
# print(today.year)
# print(today.weekday())

# now = datetime.now()
# now2 = datetime.today()

# print(now, now2, sep='\n')

# print(now.day)
# print(now.month)
# print(now.year)
# print(now.weekday())
# print(now.hour)
# print(now.minute)
# print(now.second)

# days = ['mon', 'tue', 'wen', 'thu', 'fri', 'sat', 'sun']
# print(days[now.weekday()])

# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
now = datetime.now()
# print(now.strftime('%a'))
# print(now.strftime('%A'))

# print(f'Date: {now.strftime("%A, %d %b %Y")}')
# print(f'Time: {now.strftime("%H:%M:%S")}')

# print(now.strftime("%c"))
# print(now.strftime("%x"))
# print(now.strftime("%X"))

d1 = now + timedelta(days=1, hours=2, minutes=13)
print(d1.strftime("%c"))