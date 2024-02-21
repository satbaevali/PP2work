from datetime import datetime
curren_time=datetime.now()
result_time=curren_time.replace(microsecond=0)
print("Current datetime:",curren_time.strftime("%d-%m-%Y %H:%M:%S.%f"))
print("After drop microseconds:",result_time.strftime("%d-%m-%Y %H:%M:%S"))