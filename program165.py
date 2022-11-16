class Student:
    school_name ='xyz higher secondary school'
    principal_name = 'Pro. Dr. Umesh Regmi '
    
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def get_first_name(self): # instance method 
        return self.first_name
        

    @classmethod # it is return to denote the class method
    def get_school_name(cls): # static/class method
        return cls.school_name

s = Student('umesh', ' regmi ')
print('My name is   ',s.get_first_name()) # callling the instense  method 
print('my school name is ',Student.get_school_name()) # calling the class method 
