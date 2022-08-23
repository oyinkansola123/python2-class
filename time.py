import datetime
import time
username=input("enter the name of the user")
print(username)
now=datetime.datetime.now()
print("current date and time: ")
print(time.strftime("%Y-%m-%d %H:%M:%S"))
