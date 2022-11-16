class Student:
    _school_name ='xyz higher secondary school'
    _principal_name = 'Pro. Dr. Umesh Regmi '
    
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age =age
        
    def get_first_name(self): # instance method 
        return self.first_name

a = Student('umesh', ' regmi ',28)
# a.age =-10
# print(a.age) # logic 
print(a._school_name) # understand it private but it can be accessed outside the class
#we make private by just only adding the single underscore in front of variable name 
# so , it becomes private but it can be accessed by the oursider /Hacker