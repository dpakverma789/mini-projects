
from Mini_Projects.Python_DB_ORM.orm2 import *
print("\n\t" * 3, "WELCOME TO VIRTUAL ATM")
loop = flag = True

# create_database(db_name="virtual_atm")
# create_table(db_name='virtual_atm',table_name='customer_profile',columns={
#         'account_number': 'INT',
#         'first_name': 'VARCHAR(100)',
#         'last_name': 'VARCHAR(100)',
#         'pin': 'INT',
#         'amount': 'INT',
#     })

class ATM:
    def __init__(self, customer_account_number, customer_pin, customer_current_balance):
        self.customer_account_number = customer_account_number
        self.__customer_pin = customer_pin
        self.__customer_current_balance = customer_current_balance
        self.is_authenticated = False

    @staticmethod
    def user_greeting(user):
        print(f"\n\t\thello, {user} hope you are doing well!\n".title())

    def withdraw_amount(self, withdraw_amount):
        if withdraw_amount <= self.__customer_current_balance:
            self.__customer_current_balance -= withdraw_amount
            print(f'\n\t\tyour withdraw amount is :{withdraw_amount}\n'.title())
            update_record(db_name='virtual_atm', table_name='customer_profile',
                          values={'amount': self.__customer_current_balance},
                          where=f'account_number={self.customer_account_number}')
            self.show_balance()
        else:
            print('\n\t\toops! insufficient balance!\n'.title())
        return self.__customer_current_balance

    def deposit_amount(self, deposit_amount):
        self.__customer_current_balance += deposit_amount
        print(f'\n\t\tyour deposit amount is :{deposit_amount}\n'.title())
        update_record(db_name='virtual_atm', table_name='customer_profile',
                      values={'amount': self.__customer_current_balance},
                      where=f'account_number={self.customer_account_number}')
        self.show_balance()
        return self.__customer_current_balance

    def show_balance(self):
        print(f'\n\t\tyour Current Balance is :{self.__customer_current_balance}\n'.title())

    def authentication(self, account_number, pin):
        if account_number == self.customer_account_number and pin == self.__customer_pin:
            self.is_authenticated = True
            print('\n\n{:=^40}\n'.format(' you are logged in '.title()))
        else:
            print('\n\t\tinvalid credentials\n'.title())
        return self.is_authenticated

    def change_password(self, old_password, new_password, confirm_password):
        if self.__customer_pin == old_password and self.is_authenticated:
            if new_password == confirm_password:
                update_record(db_name='virtual_atm', table_name='customer_profile',
                              values={'pin': new_password},
                              where=f'account_number={self.customer_account_number}')
                print('\n\t\tyour password has been change successfully\n')
            else:
                print("\n\t\tnew pin and confirm pin didn't match\n")
        else:
            print('\n\t\tyou entered wrong pin\n')


while loop:
    try:
        print("\nPRESS 1 FOR CREATE ACCOUNT\t\t PRESS 2 FOR LOGIN")
        option_input = int(input('Enter Your Input: '))
    except ValueError:
        print('input should in numeric value\n'.title())
        continue
    if option_input == 1:
        user_data = {'first_name': None, 'last_name': None, 'account_number': None, 'pin': None, 'amount': None}
        for i in user_data.keys():
            user_data[i] = input(f'Enter your {i}: ')
        create_record(db_name='virtual_atm', table_name='customer_profile', values=user_data)
    if option_input == 2:
        try:
            input_account_number = int(input('\n\nEnter Your Account Number: '))
            input_pin_number = int(input('Enter Your 4 digit Pin: '))
        except ValueError:
            print('password should in numeric value\n'.title())
            continue
        record = fetch_record(db_name="virtual_atm", table_name='customer_profile',
                              where=f'account_number={input_account_number}')
        if record:
            user_data = record[0]
            atm = ATM(customer_account_number=int(user_data['account_number']), customer_pin=int(user_data['pin']),
                      customer_current_balance=int(user_data['amount']))
            is_authenticated = atm.authentication(input_account_number, input_pin_number)
            if is_authenticated:
                flag = True
                atm.user_greeting(user=f'{user_data["first_name"]} {user_data["last_name"]}')
                while flag:
                    print("\nPRESS 1 FOR WITHDRAW \t\t PRESS 2 FOR PIN CHANGE\t\t PRESS 3 FOR BALANCE CHECK")
                    print("\nPRESS 4 FOR DEPOSIT \t\t PRESS 0 FOR EXIT")
                    try:
                        operation = int(input('\n\nEnter you choice: '))
                    except ValueError:
                        print('invalid choice please select correct option\n'.title())
                        continue
                    if not operation:
                        print('\n\t\t====== You have been Logged OUT ======')
                        print('\t\tThank You for using Our Virtual ATM!\n\n')
                        flag = False
                    elif operation == 1:
                        amount = int(input('Enter amount to be withdraw: '))
                        if isinstance(amount, int):
                            atm.withdraw_amount(amount)
                    elif operation == 2:
                        old_pin = int(input('Enter Your 4 digit old Pin: '))
                        new_pin = int(input('Enter Your 4 digit new Pin: '))
                        confirm_pin = int(input('Enter Your 4 digit confirm Pin: '))
                        atm.change_password(old_pin, new_pin, confirm_pin)
                    elif operation == 3:
                        atm.show_balance()
                    elif operation == 4:
                        amount = int(input('Enter amount to be deposit: '))
                        if isinstance(amount, int):
                            atm.deposit_amount(amount)
                    else:
                        print('{:=^40}\n'.format('invalid input'.title()))