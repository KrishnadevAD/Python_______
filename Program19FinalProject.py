class Bank:
    __interest_rate = 12
    __bank_name = 'Bro Bank Pvt. Ltd.'
    def __init__(self, first_name, last_name, address):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__balance = 0 
    
    def check_balance(self):
        '''this is check balance method

            arguments: none
            return current balance
        '''
        return self.__balance
    def deposit_balance(self, deposit_amount):
        if deposit_amount < 0 or str(deposit_amount).isalpha():
            print('Enter valid amount')
            return    
        self.__balance = self.__balance + deposit_amount
    
    def withdraw_balance(self, withdrawl_amount):
        if withdrawl_amount < 0 or str(withdrawl_amount).isalpha():
            print('Invalid amount')
            #raise Exception('Invalid amount') 
        elif withdrawl_amount > self.__balance:
            print(f'You can withdraw only upto {self.check_balance()}') 
        else:
            self.__balance = self.__balance - withdrawl_amount

    def get_full_name(self):
        return f'{self.__first_name} {self.__last_name}'
   
    @classmethod
    def get_interest_rate(cls):
        return cls.__interest_rate

    @classmethod
    def get_bank_name(cls):
        return Bank.__bank_name

    @classmethod
    def set_interest_rate(cls, new_rate):
        Bank.__interest_rate = new_rate
    
    @staticmethod
    def print_govt_holidays():
        print('Dashain bida is from Saturday')
        print('Tihar Bida is next month')

account = None

while True:
    print('*' * 50)
    print(f'Welcome to {Bank.get_bank_name()}')
    user_choice = input('Enter 1 to open bank account. \nEnter 2 to check balance. \nEnter 3 to deposit balance. \nEnter 4 to withdraw balance. \nEnter 5 to check interest rate. \nEnter 6 to change interest rate. \nEnter 7 to view holiday list. ')

    if user_choice == '1':
        first_name = input('Enter first name ')
        last_name = input('Enter last name ')
        address = input('Enter address ')

        if first_name.isalpha() and last_name.isalpha() and address.isalnum():
            account = Bank(first_name=first_name, last_name=last_name, address=address)

            print(f'Hi {account.get_full_name()}. An account has been created.')
        else:
            print('Please enter valid credentials.')
        
    elif user_choice == '2' and account is not None:
        print(f'Current balance is {account.check_balance()}')

    elif user_choice == '3' and account is not None:
        try:
            deposit_amount = int(input('Enter deposit amount '))
        
            account.deposit_balance(deposit_amount)
            print(f'Updated balance is {account.check_balance()}')
        except:
            print('Something went wrong. \nPlease try again later.')
    
    elif user_choice == '4' and account is not None:
        withdrawl_amount = int(input('Enter withdrawl amount '))
        account.withdraw_balance(withdrawl_amount)
        print(f'Updated balance is {account.check_balance()}')
    
    elif user_choice == '5':
        print(f"Bank's current interest rate is {Bank.get_interest_rate()}")
    
    elif user_choice == '6':
        print('*****WARNING*******')
        change_rate_choice = input('Enter 0 to exit. Enter 1 to continue. ')

        if change_rate_choice == '0':
            continue #pass
        elif change_rate_choice == '1':
            new_rate = int(input('Enter new interest rate '))
            Bank.set_interest_rate(new_rate)
            print(f'Updated interest rate is {Bank.get_interest_rate()}')

    elif user_choice == '7':
        Bank.print_govt_holidays()
    
    elif account is None:
        print('Please open an account first')
    else:
        print('Please enter valid choice')