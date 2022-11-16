class Student:
    school_name ='xyz higher secondary school'
    principal_namre ='Pro. Dr. Umesh regmi '
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def get_first_name(self):
        return self.first_name

    @staticmethod   # static method  it is marameter less and paramaterized too
    def print_govt_holiday_list(cls):
        print('teej holiday in bhadra ')

s = Student('umesh', ' regmi ')
print(s.get_first_name()) # it calls the output of the instance variable 
print(Student.print_govt_holiday_list) # it gives the addres to print the class method 4
print(Student.print_govt_holiday_list(Student)) # it gives the output of calss method 
