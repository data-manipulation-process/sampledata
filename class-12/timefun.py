#!/usr/bin/python
import time;

localtime = time.asctime(time.localtime(time.time()))
# print ("Local current time :", localtime)

#!/usr/bin/python
import calendar

cal = calendar.month(2023, 2)
print("Here is the calendar:")
print(cal)