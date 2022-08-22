
import hashlib
import os
path = os.getcwd()


class HashCrak():
    def __init__(self,default_wordlist, hashed_original_password):
        self.default_wordlist = default_wordlist
        self.hashed_original_password = hashed_original_password
        
        
    def wordlist(self):    
        result = False
        try:
            with open(self.default_wordlist, 'r', encoding='utf-8', errors='ignore') as wordlist:
                for word in wordlist:
                    word = word.strip('\n')
                    hashed_guess_password = hashlib.md5(word.encode()).hexdigest()
                    if self.hashed_original_password == hashed_guess_password:
                        result = True
                        print('\nCracked the Hash, Password is : '+word+' : '+self.hashed_original_password)
                        break
                if result == False:
                    print('\nNo Password Found for this hash :',self.hashed_original_password)
        except FileNotFoundError:
            print('OOps!! WordList Do not exist!!')


if __name__ == "__main__":
    while True:
        flg = True
        print("\n\n\nPRESS 1 FOR Single Hash Password \t\t PRESS 2 FOR Hashed Password List")
        while flg:
            try:
                choice = int(input("\nENTER YOUR CHOICE HERE :"))
                flg = False
            except:
                print('\n\t\tEnter input in Numeric Form')
        if choice in (1, 2):
            default_wordlist = input('\nEnter YOur WordList path with name if any: ')
            default_wordlist = path+'\\'+'rockyou.txt' if default_wordlist == '' else default_wordlist

        if choice == 1:
            flg = True
            while flg:
                try:
                    hashed_original_password = input('\nEnter YOur HasHed PassWord* ')
                    if hashed_original_password != '':
                        flg = False
                except:
                    print('Please input the Hashed Password!!')
            HashCrak_Obejct = HashCrak(default_wordlist, hashed_original_password)        
            HashCrak_Obejct.wordlist()
            print('\n*** Password Attack has been Completed ***')

        elif choice == 2:
            try:
                hash_list_name = input('\nEnter YOur HasHed-List path: ')
                hash_list_name = hash_list_name if 'txt' in hash_list_name else hash_list_name+'.txt'

                with open(hash_list_name, 'r', encoding='utf-8', errors='ignore') as hashlist:
                    for hashh in hashlist:
                        hashh = hashh.strip('\n')
                        HashCrak_Obejct = HashCrak(default_wordlist, hashh)
                        HashCrak_Obejct.wordlist()
                    print('\n*** Password Attack has been Completed ***')
            except FileNotFoundError:
                print('\n\tOOps!! HasHed-List Do not exist!!')
        else:
            print('\n\t\tInvalid Input!')
