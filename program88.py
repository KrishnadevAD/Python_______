# write a funtion that takes a number 10 and less and print serial number 
def num(a):
    if a>10:
        print("the number is greater then 10 ")
    else:
        return list(range(1,a+1))
result = num(10)
print(result)

    