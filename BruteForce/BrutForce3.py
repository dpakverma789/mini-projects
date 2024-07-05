voice_id_1="HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

from itertools import product
import time,string,pyautogui,pyttsx3  
from datetime import datetime
from playsound import playsound
import time,os
from threading import *
import queue

#For hard brute force
#chars = list(string.printable)

#For medium brute force attack
'''chars=['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       '`','~','!','@', '#', '$', '%', '^', '&', '*','(',')','_','-','=','+','{','}','[',']','/','?','<','>','.',',',
       '0','1','2','3','4','5','6','7','8','9']'''

#For soft brute force attack
chars=['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       '@', '#', '$', '&','0','1','2','3','4','5','6','7','8','9']

chars_reverse = sorted(chars,reverse=True)
engine = pyttsx3.init('sapi5')
key = pyautogui.password('Enter Password')
password_length = len(key)
password = tuple(key)
path = os.getcwd()

#Time Function
def date_diff_in_Seconds(dt2, dt1):
        timedelta = dt2 - dt1
        return timedelta.days * 24 * 3600 + timedelta.seconds

#Audio funtion
def speak(audio):
    engine.setProperty('rate',170)
    engine.setProperty('voice',voice_id_1)
    engine.say(audio)
    engine.runAndWait()
    return

def func(attack):
    with open('wordlist.txt','a+') as fp:
        wordlist = fp.read()
        if attack not in wordlist:
            fp.write(str(attack))
            fp.write('\n')
        print('\nDone!')
        print('\nYour PassWord is: ',attack)
        return 

#Attack Function from beginning
def brute_force():
    print('\nAttacking on Password...\n')
    for attack in product(chars, repeat=password_length):
        if attack == password:
            attack = str(''.join(attack))
            func(attack)
            return
            

#Attack Function from last
def brute_force_reverse():
    print('\nBe patient I am trying rigrously, till then take a break!!')
    for attack_reverse in product(chars_reverse, repeat=password_length):
        if attack_reverse == password:
            attack = str(''.join(attack_reverse))
            func(attack)
            return

        
date1 = datetime.now()
try:
    with open('wordlist.txt','r+') as fp:
        wordlist = fp.read()
        if key in wordlist:
            print('\nDone!!')
            print('\nYour PassWord is: ',key)
            date2 = datetime.now()
        else:
            t1 = Thread(target=brute_force_reverse)
            t1.start()
            brute_force()
            date2 = datetime.now()
except:
    t1 = Thread(target=brute_force_reverse)
    t1.start()
    brute_force()
    date2 = datetime.now()    
time_in_sec = date_diff_in_Seconds(date2, date1)
time_formate = 'seconds'
if time_in_sec > 60:
    time_formate = 'minutes'
    time_in_sec = time_in_sec/60
    if time_in_sec > 60:
        time_formate = 'hours'
        time_in_sec = time_in_sec/60
print('It took %0.2f %s to crack this password'%(time_in_sec,time_formate))
speak('Password Attack has been Completed')
playsound(path+'\\tone_alert.mp3')
pyautogui.alert(title='Status',text='Password Attack has been Completed!')






