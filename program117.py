#  this method any files opened will 
#  be closed automatically after one is done,
#   so auto-cleanup. 

# Python code to illustrate with()
with open(r"C:\Users\DELL\Desktop\python\day13\program7.txt","r") as file: 
    data = file.read()
    print(data)
# do something with data