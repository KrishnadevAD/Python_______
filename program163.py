class Student:
    school_name ='xyz higher secondary school'
    principal_name ='Pro. Dr. Umesh regmi '
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
s = Student('umesh', ' Regmi ')
print(dir(s)) # it can be done but  more unformatted output 
print('The school name is :',Student.school_name)
print('The Principal name is :',Student.principal_name)
print('First Name :',s.first_name)
print('Last name :',s.last_name)