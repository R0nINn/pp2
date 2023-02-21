# import datetime

# x = datetime.datetime.now()

# if int(x.strftime("%d")) < 6:
#     print(31 +int(x.strftime("%d")) - 5)
    
# else :
#     print(int(x.strftime("%d"))-5)

# import datetime

# today = datetime.date.today()

# x = today - datetime.timedelta(days = 5)

# print(x)

# import datetime

# today = datetime.date.today()

# yesterday = today - datetime.timedelta(days = 1)

# tomorrow = today + datetime.timedelta(days = 1)

# print(yesterday)
# print(today)
# print(tomorrow)

# import datetime

# x = datetime.datetime.now()


# print(x.strftime("%X"))

from datetime import datetime , time

def dif_in_sec(dt1,dt2):
    
    timedef = dt2-dt1
    return timedef.days * 24 *3600 + timedef.seconds    
    
date1 = datetime.strptime("2022-12-25 00:00:00" , "%Y-%m-%d %H:%M:%S" )

date2 = datetime.now()

print(dif_in_sec(date1,date2) ,"seconds")

