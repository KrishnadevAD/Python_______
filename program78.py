def add(*args):
    sum=0
    for item in args:
        sum=sum+item
    return sum
Total=add(1000,2000,3000)
print(Total)