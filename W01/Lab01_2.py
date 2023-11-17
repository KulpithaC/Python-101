#!/usr/bin/env python3
# Kulpitha Chaimongkol
# 640510639
# Lab01_2
# 229223 Sec 002

milli = int(input("Input millisecond: "))
day, dayleft = divmod(milli, 86400000)
hour, hourleft = divmod(dayleft, 3600000)
minute, minuteleft = divmod(hourleft, 60000)
second, milli = divmod(minuteleft, 1000)
print(day, " day(s)," , hour , " hour(s)," , minute , " minute(s)," , second , " second(s)," , milli , " millisec(s)")