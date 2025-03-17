
# PASSWORD GENERATOR

import random
import string
chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '@'+'#'+'$'+'!'+'%'+'&'


class PasswordGenerator:

    @staticmethod
    def pass_gen():
        password = ''
        try:
            length = int(input('\n\nENTER LENGTH OF THE PASSWORD TO BE GENERATED: '))
            for _ in range(length):
                i = random.choice(chars)
                password = password + i
            return password
        except Exception as e:
            print('\n\t ----- EXCEPT ONLY NUMERICAL VALUE -----\n', e)
 

if __name__ == '__main__':
    while True:
        passwrd = PasswordGenerator()
        print("\nYOUR GENERATED PASSWORD IS :", passwrd.pass_gen(), '\n=============\n')


