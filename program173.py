class Student:
    __school_name ='xyz higher secondary school'
    __principal_name = 'Pro. Dr. Umesh Regmi '
    
    def __init__(self,first_name,last_name,age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age =age
        
    def get_age(self): # instance method  so that we can access it called getter
        return self.__age
    
    def set_age(self,new_age):
        self.__age = new_age

a = Student('umesh', ' regmi ',28)
# a.age =-10
# print(a.age) # logic 
# print(a.get_age()) # we cannot access because it is private
a.set_age(10)
print(a.get_age()) 

