days = int(input("ENTER HOW MANY DAYS : "))

if days==0:
    cal=days*0
    print("NO FINE GOOR- ",cal,"DAYS")
elif days>=1 and days<=5:
    cal=days*1
    print("1 RUPEE FINE FOR EACH DAY-",cal,"FINE")
elif days>=5 and days<=10:
    cal=days*5
    print("5 RUPEE FINE FOR EACH DAY-",cal,"FINE")
elif days>=10 and days<=30:
    cal=days*10
    print("10 RUPEE FINE FOR EACH DAY-",cal,"FINE")
else:
    
    print("MEMBERSHIP CANCEL FOR YOU")