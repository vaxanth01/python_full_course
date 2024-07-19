mark = int(input("ENTER A MARK : "))

if mark >= 35 and mark<=100:
    print(mark >= 35 and mark <=100)
    print("hi")
    print("PASS")
else:
    print("FAIL")    
    print(not(mark >= 35 and mark<=100))


print("__________________________________")

if mark >= 35 or mark <= 100:
    print("NOT OK")
    print(mark >= 35 or mark<=100)
else:
    print("OK")    


