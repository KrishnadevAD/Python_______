class Student:
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln
        print(id(self))
s=Student('umesh','regmi')
print(id(s))
print('*********')
a=Student('ram','adhikari ')
print(id(a))

# b=Student()
s.first_name ='krishnadev '
print(s.first_name) # to call the property we need to call by . 
print(a.first_name)
# print(b.first_name)