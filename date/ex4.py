import datetime
date1 = datetime.datetime(2024, 1, 31, 15, 0, 0)
date2 = datetime.datetime(2024, 2, 15, 14, 10, 0)
difference = date2 - date1
print(difference.total_seconds())