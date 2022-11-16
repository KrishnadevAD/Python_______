class Student:
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln
s=Student('umesh','regmi')
a=Student('ram','adhikari ')
# b=Student()
print(s.first_name) # to call the property we need to call by . 
print(a.first_name)
# print(b.first_name)