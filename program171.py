class Student:
    school_name ='xyz higher secondary school'
    principal_name = 'Pro. Dr. Umesh Regmi '
    
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age =age
        
    def get_first_name(self): # instance method 
        return self.first_name

a = Student('umesh', ' regmi ',28)
a.age =-10
print(a.age) # logic 