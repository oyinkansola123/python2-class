import datetime
presentime = datetime.datetime.now()

hourNow =presentime.strftime('%H')
hourNow=int(hourNow)
print("Current Time is:", hourNow)
a=0
while a<1:
    username=(input("enter the name of the user"))
    if username.isalpha()==True:
     a=1
    else:
     print('ivalid username,enter again')
     a=0
if (hourNow)>=1 and (hourNow)<=11:
        print("Good Morning" ,username)
elif (hourNow) >=12 and (hourNow)<=16:
        print("Good Afternoon" ,username)
elif (hourNow) >=20 and (hourNow) <= 25:
        print("Good Evening" ,username)
else:
        print("we are at night")