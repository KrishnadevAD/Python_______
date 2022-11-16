while True:
    try:
        first =int(input('enter first number '))
        second =int(input('enter second number'))
        print(first/second)
        print('Dami Cha hai guys .....')
    except Exception as e: # it shows the what the exception is ???
        print(e)
    finally:
        print('Have a good day ')

# just print the number in the string