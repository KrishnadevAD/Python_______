class Student:
    school_name ='xyz higher secondary school'
    principal_namre ='Pro. Dr. Umesh regmi '
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.school_name ='xyz higher secondary school' # it occupies the more space 
        self.principal_namre ='Pro. Dr. Umesh regmi ' # it can be done but donot do it  , it occupies more space 
        
s = Student('umesh', ' regmi ')