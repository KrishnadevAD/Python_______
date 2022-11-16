while True:
    try:
        first =int(input('enter first number '))
        second =int(input('enter second number'))
        print(first/second)
        print('Dami Cha hai guys .....')
    except Exception as e: # it shows the what the exception is ???
        print(e)
        # just give the input as second number 0 
        # just give input as string