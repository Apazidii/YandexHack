import datetime
most = ["13:20", "9:12"]
print(datetime.timedelta(hours=int(most[0][:most[0].find(":")]), minutes=int(most[0][most[0].find(":") + 1:])))