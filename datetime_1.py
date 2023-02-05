import time 
import datetime
print("Current date and time:", datetime.datetime.now())
print("Current year:", datetime.date.today().strftime("%y"))
print("Month of year:", datetime.date.today().strftime("%B"))
print("Week number of the year:", datetime.date.today().strftime("%W"))
print("Weekday of the week:", datetime.date.today().strftime("%W"))
print("day of year:", datetime.date.today().strftime("%j"))
print("Day of month:", datetime.date.today().strftime("%d"))
print("day of week", datetime.date.today().strftime("%A"))