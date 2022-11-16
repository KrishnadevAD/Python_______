class Student:
    school_name ='xyz higher secondary school'
    principal_namre ='Pro. Dr. Umesh regmi '
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        print(Student.school_name)
s = Student('umesh', ' regmi ')
print(Student.school_name)
print(s.school_name) # donot write it  but call garna chai milxa hai 
