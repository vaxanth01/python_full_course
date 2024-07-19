a={1,2,3,4,5}
b={5,6,7,8,9}
c=a.intersection(b)
print(c)
d=a.union(b)
print(d)
e=a.symmetric_difference(b)
print(e)

a.intersection_update(b)
print(a)
a.update(b)
print(a)

a.symmetric_difference_update(b)
print(a)