try:
    a=b+c
except NameError as e:
    print(e)
   
try:
    a=10/0
except Exception as e:
    print(e)

try:
    a=int("gdvsc")
except Exception as e:
    print(e)

try:
    a=[2,35,65,74,3,42]
    print(a[0])
except Exception as e:
    print(e)

try:
    f=open("44try.py")
except Exception as e:
    print(e)
else:
    print(f.read())

