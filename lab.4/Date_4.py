from datetime import datetime
date_time1=datetime(2022,1,1,12,0,0)
date_time2=datetime(2022,1,1,14,30,0)
#calcukate defference second
deffent_second=(date_time2-date_time1).total_seconds()
print("Date-Time 1:", date_time1)
print("Date-Time 2:", date_time2)
print("Difference in Seconds:", deffent_second)