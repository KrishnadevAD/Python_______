class Student:
    school_name ='xyz higher secondary school'
    principal_namre ='Pro. Dr. Umesh regmi '
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_first_name(self):
        return self.first_name
     # static method  it is marameter less and paramaterized too
    @staticmethod   # This method doesnot depends on the both instance & class variable 
    def add(i,j):
        return i + j 
        
s = Student('umesh', ' regmi ')
print(s.first_name)
print(s.last_name)
print(Student.add(3,5))