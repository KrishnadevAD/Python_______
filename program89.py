 #WAP tha prints the name written in any letter to first letter capital and rest small letter 
 # umesH  to Umesh
 # UMESH to Umesh
 # UmeSH to Umesh
def capatalize_name(name):
    return 'Welcome  ' + name[0].upper() + name[1:].lower()
user_name = input("enter  yout name ")
print(capatalize_name(user_name))
