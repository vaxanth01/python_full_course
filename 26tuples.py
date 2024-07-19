a=(1,2,3,4,5,6)
print(a)
print(type(a))
b=(1,True,"helo",2.2)
print(b)
print(type(b[1]))
print(type(b[2]))

print(a[2:])
print(a[2:5])
print(b)
c=list(b)
print(c)
print(type(c))

for i in a:
    print(i)

if "helo" in b:
    print("found")
else:
    print("not found")    


d=(a,b)
print(d)
e=("joes",)*10
print(e)

print(min(a))
print(max(a))