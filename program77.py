def add(*args):
    sum=0 # local declaration, it can be accessed only inside the local funtion 
    for item in args:
        sum=sum+item
    if sum>20000:
        print("buy big khasi")
    else:
        print("small khasi ")
add(1000,2000,3000)
    
