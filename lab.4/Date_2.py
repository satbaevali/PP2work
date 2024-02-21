from datetime import datetime,timedelta
today_time=datetime.now()
yesterday_date=today_time-timedelta(days=1)
tomoraw_date=today_time+timedelta(days=1)
print("Today:",today_time.strftime("%d-%m-%Y"))
print("Yesterday:",yesterday_date.strftime("%d-%m-%Y"))
print("Tomorow:",tomoraw_date.strftime("%d-%m-%Y"))