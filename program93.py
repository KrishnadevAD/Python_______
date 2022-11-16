while True:
    try:
        first =int(input('enter first number '))
        second =int(input('enter second number'))
        print(first/second)
        print('Dami Cha hai guys .....')
    except ZeroDivisionError:
        print('The number cannot divided by Zero')
    except TypeError:
        print('Number cannot be converted into one type to another type')