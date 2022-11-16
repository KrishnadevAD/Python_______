students = [2,3,4,5,6,7,8]
print(students)
students.insert(2,'krishnadev adhikari ') # it inset the value at the index 2 of list 
print(students)
students.remove('krishnadev adhikari ')
print(students) # it again removes the krishnadev adhikari 
students.remove('krishnadev  ') # ValueError: list.remove(x): x not in list because there is no krishnadev in list
print(students) # it again removes the krishnadev adhikari 