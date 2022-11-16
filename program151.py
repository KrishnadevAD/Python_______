class Student:
    def __init__(self,fn,ln):
        self.first_name = fn
        self.last_name = ln
        print(self.first_name)

s= Student('Krishna Dev ','Adhikari ')
print(s.first_name)