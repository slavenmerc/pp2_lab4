from datetime import datetime, timedelta
x = datetime.now()
print(x.strftime("%Y"), x.strftime("%m"),x.strftime("%d"), sep ="-", end = " ")
print(x.strftime("%X"))