from ast import arg
from re import A


def add(*args):
    sum=0
    for item in args:
        sum=sum+item
    return sum
def mean(*args):
    sum=add(*args)
    avg=sum/len(args)
    print(avg)
mean(1000,2000,3000)