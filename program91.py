 #exception handeling 
 
while True:
    try:
        first =int(input('enter first number '))
        second =int(input('enter second number'))
        print(first/second)
    except:
        print('There is an error')
        print('Please try again later')