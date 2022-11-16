def is_even(n):
    return n%2==0
a=list(filter(is_even,[1,2,3,4,5,6,7,8,9])) # filter returns the object so put in the list 
a=list(filter(lambda n :n%2 ==0,[1,2,3,4,5,6,7,8,9])) # filter returns the object so put in the list 
print(a)
