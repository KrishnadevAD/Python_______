#polymorphism
 # ineritance 
 # code without inheritance 

class Employee:
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
   

class fullTimeEmployee(Employee): #it is also called 'is a relationship
    pass


   
class PartTimeEmplpyee(Employee):
    pass
   
f= fullTimeEmployee('ram','adhiakri',2500)
p= PartTimeEmplpyee('umesh','regmi',20)
f.add()



       
    