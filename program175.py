class Student:
    __school_name ='xyz higher secondary school'# by adding double underscore making it private 
    __principal_name = 'Pro. Dr. Umesh Regmi '
    
    def __init__(self,first_name,last_name,age):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age =age
        
    def get_age(self): # instance method  so that we can access it called getter
        return self.__age # getter returns the value and takes only one parameter called self

    
    def set_age(self,new_age): # it is called setter , and it takes 2 paramater
        self.__age = new_age # setter changes the value 
                            # we can take multiple parameter but take only which we want to change 

    @classmethod
    def get_school_name(cls): # making the class variable as the  Getter 
        return cls.__school_name

    @classmethod
    def set_school_name(cls,new_name): # making the class method as the Setter
        cls.__school_name=new_name
        

a = Student('umesh', ' regmi ',28)
# a.age =-10
# print(a.age) # logic 
# print(a.get_age()) # we cannot access because it is private
a.set_age(10) # it goes to func. set_age and 'a' gets to  self and self.__age == 10 ==new_age 
              # previously we have __age == 28 and , after that it will become self.__age == 10 ==new_age
print(a.get_age()) # now here we have called a.get_age() function so it will go into it and 
# in self we have 'a' , we get return as a.__age (we have __age == 10 )
# so it will return the value 10 
Student.set_school_name('sxy school')
print(Student.get_school_name())
