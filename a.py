import datetime
import calendar
import os
import random

n = 100
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
wd = {"Sunday":"Sun","Monday":"Mon","Tuesday":"Tue","Wednesday":"Wed","Thursday":"Thur","Friday":"Fri","Saturday":"Sat"}

def wdcal(n):
    for i in wd:
        if i == n:
            return wd[i]

def mounthcal(n):
    n = n-1
    return months[n]

for i in range(n):
    a = datetime.datetime.today()-datetime.timedelta(days=5)
    Previous_Date = a - datetime.timedelta(days=i)
    print(Previous_Date)
    date = Previous_Date.day
    # print(date)
    date = str(date)
    month = (mounthcal(Previous_Date.month))
    # print(month)
    week = wdcal(str(calendar.day_name[Previous_Date.weekday()]))
    # print(week)
    times = random.randrange(1, 2)
    f = open("temp.txt", "a")
    # print("working on" + date + week + month)
    for j in range(times):
        f.write("print('hello')")
        f.write("print('hello')")
        f.write("print('hello')")
        os.system("git add .")
        commit = "git commit  --date '{} {} {} 1:00 2021 +0100' -m 'minor changes'".format(week, month, date)
        os.system(commit)
        cmd = "git push origin master"
        value = os.system(cmd)

print("done!")
