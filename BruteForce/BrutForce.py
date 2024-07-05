import random
import string
from datetime import datetime, time
try:
    import pyautogui
except:
    import os
    os.system('pip install pyautogui')
    import pyautogui

characters = string.printable
character_list = list(characters)
guess_password = ""
password = pyautogui.password('Enter Password: ')


try:
    def date_diff_in_Seconds(dt2, dt1):
        timedelta = dt2 - dt1
        return timedelta.days * 24 * 3600 + timedelta.seconds
    
    date1 = datetime.now()
    count = 0
    print('Attacking for Password...')
    while(guess_password != password):
        guess_password = random.choices(character_list, k=len(password))
        #print('--------- '+str(guess_password)+' ---------')
        count += 1
        if count == 5000000:
            print('\nIt may take time, Till then take a break!!')
        if count == 70000000:
            print('\nI am rigorously attacking, give me few more time!!\n')

        if (guess_password == list(password)):
            date2 = datetime.now()
            print('\nDone!')
            print('\nYour PassWord is : ',''.join(guess_password))
            break
        
    time_in_sec = date_diff_in_Seconds(date2, date1)
    time_formate = 'seconds'
    if time_in_sec > 60:
        time_formate = 'minutes'
        time_in_sec = time_in_sec/60
        if time_in_sec > 60:
            time_formate = 'hours'
            time_in_sec = time_in_sec/60
        
    print('I had tried %d combinations and %0.2f %s to crack it, but I did it'%(count,time_in_sec,time_formate))
    pyautogui.alert(title='Status',text='Password Attack has been Completed!')
except:
    print('\nOperation has been Stopped!!')







