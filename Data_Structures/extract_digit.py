str_1="p2r4a7n6a9ny"
digit_list=[]
for char in str_1:
    if char.isdigit():
        digit_list += [int(char)]
print(digit_list)
print(min(digit_list))
print(max(digit_list))
print(sum(digit_list))
print(sorted(digit_list))
print(sorted(digit_list,reverse=True))
