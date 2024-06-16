set_a={1,2,3,4}
set_b={3,4,5,6}
symmetric=set_a ^ set_b 
print(symmetric)
list_a=[1,2,3,4,"red"]
difference=set_a.symmetric_difference(list_a)
print(difference)
str_a="black"
diff=set_a.symmetric_difference(str_a)
print(diff)