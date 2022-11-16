class NMB: # nmb class i created 
    Bank_name = 'NMB'# it is static class variable
    Headquarter = 'lalitpur' # it is satatic class variable

    def __init__(self,first_name,last_name,age): #init method --> function defined inside class
        self.first_name = first_name # self paramater call the particular obj first name 
        self.last_name = last_name
        self.age =age
nmb =NMB('krishnadev ','adhikari',25) #NMB()-->obje is created o
print('Bank name is :',NMB.Bank_name)
print('Bank headquarter is :',NMB.Headquarter)
print('First name :',nmb.first_name)
print('last name :',nmb.last_name)
print('Age : ',nmb.age)

class NIC_ASIA:
    Bank_name = 'NIC_ASIA'
    Slogan = 'Bank pani Sathi pani '
    Headquarter = 'Kathmandu '

    def __init__(self,first_name,last_name,Baau_ko_name):
        self.first_name = first_name
        self.last_name = last_name
        self.Baau_ko_name =Baau_ko_name

nic_asia =NIC_ASIA('krishnadev ','adhikari','Ram')
print('Bank name is :',NIC_ASIA.Bank_name)
print('Bank slogan is :',NIC_ASIA.Slogan)
print('Bank Headquarter is :',NIC_ASIA.Headquarter)
print('First name : ',nic_asia.first_name)
print('Last name :',nic_asia.last_name)
print('Baau ko name :',nic_asia.Baau_ko_name)

        
        