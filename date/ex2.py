from datetime import datetime, timedelta
x = datetime.now()
yesterday = x - timedelta(days = 1)
tomorrow = x + timedelta(days = 1)
print("Yesterday -", yesterday.strftime("%x"))
print("Today -", x.strftime("%x"))
print("Tomorrow -", tomorrow.strftime("%x"))
