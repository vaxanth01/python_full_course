mark1=int(input("ENTER MARK 1 :"))
mark2=int(input("ENTER MARK 2 :"))
mark3=int(input("ENTER MARK 3 :"))
mark4=int(input("ENTER MARK 4 :"))

total = mark1+mark2+mark3+mark4
average = total/4.0
print("TOTAL :",total)
print("AVERAGE :",average)
if mark1 >=35 and mark2 >=35 and mark3 >=35 and mark4 >=35:
    print("PASS")
    if average >= 90 and average<= 100:
        print("A GRADE")
    elif average >= 80 and average<= 89:
        print("B GRADE")           
    elif average >= 70 and average<= 79:
        print("C GRADE")           
    elif average >= 60 and average<= 69:
        print("D GRADE")
    else:
        print("JUST PAS")     
            
else:
    print("FAIL")    