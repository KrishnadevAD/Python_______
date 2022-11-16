from logging import exception


try:
    f=open('program3.txt','r')
    line = f.readline()
    for line in lines:
        print(line)
except FileNotFoundError:
    print('file not found')
 # when you donot make the file and just call for the file 
# than it will   donot run on the try block as it will run the except  block