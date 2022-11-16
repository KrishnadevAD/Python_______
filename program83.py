salary = 5000
def increase_salary():
    global salary # Global variable declaration
    salary = 200000
    print(salary) # it prints out the salary of the function 
increase_salary() # it calls the increse salary function and 
print(salary) # it prints the increses salary function's salary 
