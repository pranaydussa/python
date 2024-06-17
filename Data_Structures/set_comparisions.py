set_a={1,2,3,4}
set_b={3,4}
a=set_b.issubset(set_b)
b=set_a.issuperset(set_a)
c=set_a.isdisjoint(set_b)
print(a)
print(b)
print(c)