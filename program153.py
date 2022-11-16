class Student:
    school_name = 'Khwopa Engineering College ' # static/class variable 
    address = ' Bhaktapur , Nepal'# it is just defined below the class 
    def __init__(self,fn,ln):
        self.first_name = fn # first_name is instance/object variable because it's value is changed acc. to obj
        self.last_name = ln # last_ name is also instance/object variable
        print(Student.school_name)# accessing the static variable inside the class 
        print(Student.address)# just use class name (dot) static variable name <-----

s= Student('Krishna Dev ','Adhikari ')
a= Student('Umesh','regmi')
print(s.first_name)
print(Student.school_name) # whenever we print the static variable print by using it's 
print(Student.address) # .... class name with . ( dot ) and particular one to print 