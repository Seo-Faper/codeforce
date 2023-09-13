import datetime

timestamp = 1690557597
datetime_obj = datetime.datetime.fromtimestamp(timestamp)

formatted_datetime = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_datetime)