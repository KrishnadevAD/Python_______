# WAP to print odd or even using function 
def even(a):
    if a%2==0:
        print("it is even")
    else:
        print(" it is Odd")
even(int(input("enter a number :")))

def is_even(a):
    if a%2==0:
        return True
    else:
        return False
while True: # it always takes the input from the user 
    a=int(input('enter a number'))
    result=is_even(a)
    if result== True:
        print(f'{a} is even')
    else:
        print(f'{a} is odd')
