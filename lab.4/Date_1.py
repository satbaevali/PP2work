from datetime import datetime,timedelta
current_date=datetime.now()
result_date=current_date-timedelta(days=5)
print("Curret Date:",current_date.strftime("%d-%m-%Y"))
print("Date after substracting five days:", result_date.strftime("%Y-%m-%d"))