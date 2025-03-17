

def set_in_dataBase(mycursor,password,count,simple_text):
    try:
        mycursor.execute("create database if not exists HashStore")
        mycursor.execute("USE HashStore")
        sql="CREATE TABLE if not exists HashList(Id int, text varchar(200), hash VARCHAR(200))"
        mycursor.execute(sql)
        sql = "insert into HashList(id,text,hash) values (%s,%s,%s)"
        val = (count,simple_text,password)
        mycursor.execute(sql,val)
        print("\n\t\t\tUpdated Hashh key in database!!\n\n")
    except Exception as e:
        print(e)
    finally:
        mydb.commit()
        mydb.close()
    return


def get_from_dataBase(mycursor,encrypted_text):
    try:
        mycursor.execute("USE HashStore")
        mycursor.execute("select text from HashList where hash = '{}'".format(encrypted_text))
        myresult=mycursor.fetchall()
        for x in myresult:
            print('\n\t\t\tDecrypted Password is: ',x[0],'\n\n')
        if myresult == []:
            print('\n\t\t\tNo Matching Hash Password Found in DataBase!!\n\n')    
    except Exception as e:
        print(e)
    finally:
        mydb.commit()
        mydb.close()
    return 


def passEncrpt(simple_text,concat_data,key='q'):
    try:
        for i in simple_text:
            if i.isalpha():
                ascii_pass_encrypt = ord(i)
                binary_pass = hex(ascii_pass_encrypt)
            elif i.isnumeric():
                binary_pass = hex(int(i))
            else:
                ascii_pass_encrypt = ord(i)
                binary_pass = hex(ascii_pass_encrypt)
            concat_data += binary_pass[2:]+key
        print('\n\t\tYour EnCrypted Password is: ',concat_data,'\n')

    except:
        print('\n\t\t\tEnCryption Failed!!\n\n')
    return concat_data


def passDecrypt(password_Encrypted,password,key='q'):
    splited_password = password_Encrypted.split(key)[:-1]
    return splited_password,loopKey(splited_password,password,password_Encrypted)


def loopKey(splited_password,password,password_Encrypted):
    alpha_passord = ''
    sample = ['!','@','#','$','%','^','&','*','(',')','-']
    sample2 =['_','+','=','[',']','{','}','"',"'"]
    try:
        for x in splited_password:
            concat_data = int(x,16)
            flag = chr(int(concat_data))
            if flag.isalpha():
                ascii_pass_decrypt = str(flag)
                alpha_passord += ascii_pass_decrypt
            elif flag in sample or flag in sample2:
                ascii_pass_decrypt = str(flag)
                alpha_passord += ascii_pass_decrypt
            else:
                alpha_passord += str(concat_data)
        OrignalPassword = alpha_passord
       
        if  password != password_Encrypted:
            print('\n\t\t\tWARNING! EnCrypted password has been modified\n\n')
        else:
            print('\n\t\t\tYour Decrypted Password is: ',OrignalPassword,'\n\n')
    except:
        print('\n\t\t\tDecryption Failed!!\n\n')
    return
        
try:
    import mysql.connector
    import hashlib
    import random
    import os
except:
    import os
    pack = ['mysql.connector']
    for package in pack:
        os.system(f'pip install {package}')

print("\n")
concat_data = ''
count = 0

if __name__ == '__main__':
    hash = 'cecff118d197c988ada7067733a45863'
    while(True):
        try:
            password = os.environ['database_password']
            mydb = mysql.connector.connect(host="localhost",user="root",passwd=password)
            mycursor=mydb.cursor()
            print('\n\t\t\t\tDataBase Connected!!\n')
        except:
            print('\n\t\t\t\tDatabase Connection Failed!!\n')
            print('\t\t"Warning! Your Encrypted Password will not save in Database"\n')
        try:
            choice = int(input("\nPRESS 1 FOR Password EnCryption  \t\t PRESS 2 FOR Password Decryption : "))
            if choice == 1:
                count += 1
                simple_text = input('\nEnter Your Password: ')
                password = passEncrpt(simple_text,concat_data)
                try:
                    set_in_dataBase(mycursor,password,count,simple_text)
                except:
                    print('\t\tUnable to Save Password in Database!!\n\n')
            elif choice == 2:
                encrypted_text = input('\nEnter Your Encrypted Password: ')
                try:
                    paswrd = input('\n\t\tEnter the Master-Password: ')
                    if hash == hashlib.md5(paswrd.encode()).hexdigest():
                        password_Decrypted = passDecrypt(encrypted_text,password)
                    else:
                        print('\n\t\tInvalid Master-Password!')
                except:
                    try:
                        get_from_dataBase(mycursor,encrypted_text)
                    except:
                        print('\n\t\t\tNo Matching Hash Password Found!!\n\n')
            else:
                print('\n\t\t\t\tInvalid Request!!\n\n')
        except:
            print('\n\t\t\tEnter your Choice first!!\n\n')



           





    



