def check(num1,num2,num3):
    if (num1 >= num2) and (num1 >= num3):
        print('largest ',num1)
    if(num2 >= num1) and (num2 >= num3):
        print('largest ',num2)
    if(num3>=num1) and (num3>num2):
         print('largest ',num3)
check(2,3,6)