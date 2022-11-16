f = open(r'C:\Users\DELL\Desktop\python\day13\program2.txt','r')
print(f.read())
# f.write('mero name krishnadev adhikari ho hai guys ... ')
# f.write('eh sathi timi kaha xau bhana na , lamo din haru katnu nai garho ')
lines = f.readline()
for item in lines:
    print(lines)