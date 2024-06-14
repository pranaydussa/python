def multiple(x):
    if x==1:
        return 1
    return x*multiple(x-1)


n=int(input())
result=multiple(n)
print(result)