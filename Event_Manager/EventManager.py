
# EVENT MANAGER
import os
from datetime import datetime
from time import *
from playsound import playsound

original_working_directory = os.getcwd()
os.chdir('F:\python_programs\Event_Manager')
song = os.path.join(os.getcwd(), 'happy_birthday_tone.mp3')
now = datetime.now()
d = now.strftime("%d-%B-%Y")
d = d.split('-')


def addEvent():
    count = 0
    if os.stat(os.path.join(os.getcwd(), "count.txt")).st_size != 0:
        with open(os.path.join(os.getcwd(), "count.txt"), 'r') as fpc:
            count = fpc.readline()
    number_of_event=str(1+int(count))
    try:      
        with open(os.path.join(os.getcwd(), "EventManager.txt"), 'a+') as fp:
            event, name, date, month = input("\nEnter 'EVENT' 'NAME' 'DATE' and 'MONTH' : ").split()
            text = ','+event+',', ','+name+',', ','+date+',', ','+month+',', ','+number_of_event+','
            event_as_list = list(text)
            event_as_str = str(event_as_list)
            fp.write(event_as_str.title())
            fp.write('\n')
            with open(os.path.join(os.getcwd(), "count.txt"), 'w+') as fpc:
                fpc.write(number_of_event)
            print('\nEvented Added: ', event_as_str.title(), '\n')
            return
    except:
        print('"Expected!" EVENT, NAME, DATE and MONTH as Example:')
        print("Birthday Jarvis 06 July")
    os.chdir(original_working_directory)
    return


def showEvent():
    if os.stat(os.path.join(os.getcwd(), "EventManager.txt")).st_size == 0:
        print('File is Empty')
    else:
        with open(os.path.join(os.getcwd(), "EventManager.txt"), 'r') as fp:
            fp.seek(0)
            event_data = fp.read()
            print(event_data)
    os.chdir(original_working_directory)
    return


def checkEvent():
    number_of_event = index_range = flag = 0
    with open(os.path.join(os.getcwd(), "EventManager.txt"), 'r') as fp:
        fp.seek(0)
        event_data = str(fp.read())
        list = event_data.split(',')
        if os.stat(os.path.join(os.getcwd(), "count.txt")).st_size != 0:
            with open(os.path.join(os.getcwd(), "count.txt"), 'r') as fpc:
                count = fpc.readline()
        if os.stat(os.path.join(os.getcwd(), "EventManager.txt")).st_size == 0:
            os.chdir(original_working_directory)
            print('\t\t\t"No Event Found!!"')
            return
        number_of_event = int(count)
        index_range = number_of_event*14
        for i in range(7, index_range, 14):
            if list[i] == d[0] and list[i+3] == d[1]:
                flag = True
                break
        if flag:
            print('\t\t\t"Wish!!', list[i-3], 'HaPpY', list[i-6], 'As On', list[i], list[i+3]+'"')
            playsound(song)
        else:
            print('\t\t\t"No Event Found!!"')
    os.chdir(original_working_directory)
    return


def clearEvent():
    with open(os.path.join(os.getcwd(), "count.txt"), 'w+') as fpc, open(os.path.join(os.getcwd(), "EventManager.txt"), 'w+') as fp:
        fpc.truncate(0)
        fp.truncate(0)
        print("Data Cleared!")
    os.chdir(original_working_directory)
    return

'''
while(True):
    newFlag = 0
    choice = int(input('entr: '))
    if choice ==1:
        number_of_event = int(input('Enter number of events to be saved: '))
        for i in range(1,number_of_event+1):
            addEvent()
    if choice == 2:
        showEvent()
    if choice ==3:
        checkEvent()  
'''






