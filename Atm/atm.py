
import os
import json

print("\t"*3, "WELCOME TO VIRTUAL ATM")
user_data = open(os.path.join(os.getcwd(), 'user_account.txt'), 'r', encoding='utf-8')
user = json.loads(user_data.readline())
user_data.close()
loop = flag = True


class ATM:
    def __init__(self, username, pin, current_balance):
        self.username = username
        self.__pin = pin
        self.__current_balance = current_balance
        self.is_authenticated = False

    def user_greeting(self, user):
        print(f"\n\t\thello, {user} hope you are doing well!\n")

    def withdraw_amount(self, withdraw_amount):
        if withdraw_amount <= self.__current_balance:
            self.__current_balance -= withdraw_amount
            self.show_balance()
        else:
            print('\n\t\toops! insufficient balance!\n'.title())
        return self.__current_balance

    def deposit_amount(self, deposit_amount):
        self.__current_balance += deposit_amount
        self.show_balance()
        return self.__current_balance

    def show_balance(self):
        print(f'\n\t\tyour Current Balance is :{self.__current_balance}\n'.title())

    def authentication(self, user, passkey):
        if user == self.username and passkey == self.__pin:
            self.is_authenticated = True
            print('\n\n{:=^40}\n'.format(' you are logged in '.title()))
        else:
            print('\n\t\tinvalid credentials\n'.title())
        return self.is_authenticated

    def change_password(self, old_password, new_password, confirm_password):
        if self.__pin == old_password and self.is_authenticated:
            if new_password == confirm_password:
                fp = open(os.path.join(os.getcwd(), 'user_account.txt'), 'w+', encoding='utf-8')
                user.update({'pin': new_pin})
                fp.write(json.dumps(user))
                fp.close()
                print('\n\t\tyour password has been change successfully\n')
            else:
                print("\n\t\tnew pin and confirm pin didn't match\n")
        else:
            print('\n\t\tyou entered wrong pin\n')


while loop:
    try:
        name = input('\n\nEnter Your Name: ')
        key = int(input('Enter Your 4 digit Pin: '))
    except ValueError:
        print('password should in numeric value\n'.title())
        continue
    atm = ATM(user['username'], int(user['pin']), int(user['balance']))
    is_authenticated = atm.authentication(name, key)
    if is_authenticated:
        atm.user_greeting(user['username'])
        while flag:
            print("\nPRESS 1 FOR WITHDRAW \t\t PRESS 2 FOR PIN CHANGE\t\t PRESS 3 FOR BALANCE CHECK")
            print("\nPRESS 4 FOR DEPOSIT \t\t PRESS 0 FOR EXIT")
            try:
                operation = int(input('\n\nEnter you choice: '))
            except ValueError:
                print('invalid choice please select correct option\n'.title())
                continue
            if not operation:
                print('\n\t\tThank You for using Our Virtual ATM!\n\n')
                flag = False
            elif operation == 1:
                amount = int(input('Enter amount to be withdraw: '))
                if isinstance(amount, int):
                    net_balance = atm.withdraw_amount(amount)
                    with open(os.path.join(os.getcwd(), 'user_account.txt'), 'w+', encoding='utf-8') as file:
                        user.update({'balance': net_balance})
                        file.write(json.dumps(user))

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
                    net_balance = atm.deposit_amount(amount)
                    with open(os.path.join(os.getcwd(), 'user_account.txt'), 'w+', encoding='utf-8') as file:
                        user.update({'balance': net_balance})
                        file.write(json.dumps(user))
            else:
                print('{:=^40}\n'.format('invalid input'.title()))


