from unicodedata import name


a={'umesh':28,'ram':35,'Hari':33}
while True:
    name=input('Enter your name ').lower()
    print(f'Hi {name.capitalize()}. Your marks is {a[name]}')