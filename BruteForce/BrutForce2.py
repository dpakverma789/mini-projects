import os
from itertools import product
from datetime import datetime
try:
    import pyautogui
    import pyttsx3
    from playsound import playsound
except ModuleNotFoundError:
    for pack in ('pyautogui', 'pyttsx3', 'playsound'):
        os.system('pip install {pack}'.format(pack=pack))
    import pyautogui
    import pyttsx3
    from playsound import playsound


voice_id_1 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"

# chars = list(string.printable)
'''chars=['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       '`','~','!','@', '#', '$', '%', '^', '&', '*','(',')','_','-','=','+','{','}','[',']','/','?','<','>','.',',',
       '0','1','2','3','4','5','6','7','8','9']'''

chars = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
       'A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       '@', '#', '$', '%', '&', '*','0','1','2','3','4','5','6','7','8','9']

engine = pyttsx3.init('sapi5')
key = pyautogui.password('Enter Password')
password_length = len(key)
password = tuple(key)
path = os.getcwd()


# Time Function
def date_diff_in_Seconds(dt2, dt1):
    timedelta = dt2 - dt1
    return timedelta.days * 24 * 3600 + timedelta.seconds


# Audio function
def speak(audio):
    engine.setProperty('rate', 170)
    engine.setProperty('voice', voice_id_1)
    engine.say(audio)
    engine.runAndWait()
    return


# Attack Function
def brute_force():
    for attack in product(chars, repeat=password_length):  
        if attack == password:
            with open('wordlist.txt','a+') as wordlist:
                wordlist.write(str(''.join(attack)))
                wordlist.write('\n')
            date2 = datetime.now()
            attack = ''.join(attack)
            print('\nDone!!\nYour PassWord is: ',attack)
            return date2


print('\nAttacking on Password...')
date1 = datetime.now()
try:
    with open('wordlist.txt','r+') as wordlist:
        wordlist = wordlist.read()
        if key in wordlist:
            print('\nDone!!\nYour PassWord is: ',key)
            date2 = datetime.now()
        else:
            date2 = brute_force()
except:
    date2 = brute_force()         
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
pyautogui.alert(title='Status', text='Password Attack has been Completed!')
