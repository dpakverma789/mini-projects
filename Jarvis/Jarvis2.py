# Constants
ZIRA = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
DAVID = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
MUSIC_CATEGORY = ('D:\Music\Coders','D:\Music\Dark','D:\Music\Devotional','D:\Music\High Notes','D:\Music\Low Notes')
GREET_RESPONSE = ('i am fine how are you', 'i am doing great', 'i am awesome hope you are doing good', 'hello sir')
TIMER = 60
START_NOTE = '\nI CAN PLAY MUSIC, SET ALARM, BROWSE WIKIPEDIA, BROWSE GOOGLE, BROWSE YOUTUBE OPEN BROWSER, SEND EMAIL SHOW DATE-TIME, CALENDAR, OPEN CALCULATOR, \
PLAY GAME, HANDLE EVENT MANAGER AND SHUTDOWN SYSTEM\n\n(Say "do nothing" to put me on wait for few minute)\n'

TEXT = 'i can play music, set alarm, browse wikipedia, browse google, browse youtube, open browser, send email, show datetime and calendar,\
i can also open calculator, play game, handle event manager, change my voice and shutdown system )'

# Built-In Libraries
import os
import random
import sys
import calendar
import string
from datetime import time, datetime
from time import *
import smtplib
from threading import *
import threading


try:
    # Importing Module
    import pyttsx3
    import webbrowser
    import speech_recognition as sr
    from playsound import playsound
    import wikipedia
    from googlesearch import search
    from email.mime.text import MIMEText
    # User-Define Libraries
    from Month import *
    from TicTac_AI import *
    from EventManager import *
    from alarm import *
    from quiz_Game import get_question
except ModuleNotFoundError:
    with open(os.path.join(os.getcwd(), 'requirement.txt')) as file:
        package = [pack.strip('\n') for pack in file.readlines()]
    for pack in package:
        os.system(f'pip install {pack}')
    import pyttsx3
    import webbrowser
    import speech_recognition as sr
    from playsound import playsound
    import wikipedia
    from googlesearch import search
    from email.mime.text import MIMEText
    # User-Define Libraries
    from Month import *
    from TicTac_AI import *
    from EventManager import *
    from alarm import *
    from quiz_Game import get_question

# creating speak engine constructor
engine = pyttsx3.init('sapi5')


# time function
def time_function():
    now = datetime.now()
    x = now.strftime("%H:%M")
    y = now.strftime("%A %d-%B-%Y")
    d = now.strftime("%m-%Y")
    return x, y, d


# greeting function
def greeting():
    time, date, d = time_function()
    if time < '12:00':
        speak("Good morning sir")
    elif '16:00' > time >= '12:00':
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak('how are you')
    return


# help function
def jarvis_help():
    print(START_NOTE)
    speak(TEXT)
    print('For searching anything on wikipedia, Say! search for "your search object"\n')
    speak('For searching anything on wikipedia, Say! search for your search object')
    print('For searching anything on google, Say! google "your search object"\n')
    speak('For searching anything on google, Say! google your search object')
    print('You can also talk to me like how are you,goodbye,who are you,what can you do,you can also introduce me with your friend,we can play game,\
say change your voice')
    return


# Audio funtion
def speak(audio):
    engine.setProperty('rate', 175)
    engine.setProperty('voice', voice_id)
    engine.say(audio)
    engine.runAndWait()
    return


# Listening function
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 3500
        count = False
        counter = 1
        command = None
        while not count:
            print("I am Listening...")
            speak("I am Listening")
            r.pause_threshold = 1
            audio = r.listen(source)
            print("Give me a Moment!!")
            speak("give me a moment")
            try:
                command = r.recognize_google(audio, language="en-in")
                print("You said :" + command + "!\n")
                count = True
                command = command.lower()
            except sr.UnknownValueError:
                print("Could not understand please say it again!!")
                underline()
                speak("Could not understand please say it again")
                count = False
                counter += 1
                if counter >= 4 and command == None:
                    print("Due to no response I am turning Off!!")
                    speak("due to no response i am turning off")
                    os._exit(0)
    return command


# email function
def email(Message, To, Subject):
    try:
        body = Message
        msg = MIMEText(body)
        msg['from'] = 'dpakverma1234@gmail.com'
        msg['to'] = To
        msg['Subject'] = Subject
        print("WAIT FOR A MOMENT")
        speak("wait for a moment")
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login('dpakverma1234@gmail.com', "urlove4mine")
        server.send_message(msg)
        print("MAIL SENT SUCCESSFULLY!")
        speak("MAIL SENT SUCCESSFULLY")
    except:
        print("\nMAIL SENT FAILED\n\nMight be the Follwing Reason:\n")
        print("Check your InterNet Connectivity")
        print("Please Check the Less secure device feature turned it ON")
        speak("MAIL SENT FAILED")
        speak("Might be the Follwing Reason")
    else:
        server.quit()
    finally:
        speak("what else can i do")
    return


# music function
def music():
    music_category_index = random.randint(0, len(MUSIC_CATEGORY)-1)
    music_list = os.listdir(MUSIC_CATEGORY[music_category_index])
    music_index = music_list[int(random.randint(0, len(music_list)-1))]
    music_directory = MUSIC_CATEGORY[music_category_index]
    try:
        playsound(os.path.join(music_directory, music_index))
    except:
        music()


def underline():
    print("------------\n")
    return


# main function
if __name__ == "__main__":
    voice_id = DAVID
    checkEvent()
    speak('my name is jarvis version 3.1')
    greeting()
    print(START_NOTE)
    speak(TEXT)
    speak("what can i do for you")
    print('For any assistance say help!\n\n')
    speak('\nFor any assistance say help')

    if os.stat(os.path.join(os.getcwd(), "EventManager.txt")).st_size != 0:
        checkEvent()
        print('\n')

    out = 1
    while True:
        try:
            command = listen()
            if 'how are you' in command or 'hello' in command:
                status = random.randint(0, len(GREET_RESPONSE)-1)
                speak(GREET_RESPONSE[status])
                speak("whats your plan for today")
                underline()

            elif 'music' in command or 'songs' in command or 'song' in command:
                try:
                    speak("playing music sir, enjoy!")
                    t2 = Thread(target=music)
                    t2.start()
                    sleep(2)
                    speak("what else can i do")
                    underline()
                except:
                    print('May be you need to change the directory as per your system!')
                    speak('May be you need to change the directory as per your system')

            elif 'voice' in command:
                voice_id = DAVID if voice_id == ZIRA else ZIRA

            elif 'do nothing' in command or 'nothing' in command:
                if TIMER == 60:
                    speak('going for a one minute sleep')
                    print('I WILL BE RIGHT BACK IN 1 MINUTE')
                    underline()
                    sleep(TIMER)
                    TIMER += 60

                elif TIMER == 120:
                    speak('going for a two minute sleep')
                    print('I WILL BE RIGHT BACK IN 2 MINUTE')
                    underline()
                    sleep(TIMER)
                    TIMER += 60

                elif TIMER == 180:
                    speak('going for a three minute sleep')
                    print('I WILL BE RIGHT BACK IN 3 MINUTE')
                    underline()
                    sleep(TIMER)
                    TIMER = 60

            elif 'alarm' in command or 'reminder' in command:
                time, date, d = time_function()
                t1 = Thread(target=alarm, args=[time])
                t1.start()
                sleep(15)
                speak("what else can i do")
                underline()

            elif 'goodbye' in command or 'bye' in command:
                if time >= '20:00' and time < '04:00':
                    print("Good night")
                    speak("Good night and")
                print('Good bye, See you Soon!!')
                speak("good bye sir, see you soon")
                underline()
                break

            elif 'who are you' in command:
                print(
                    'I am an AI named Jarvis made in Python by Deepak\n I used 15 module and 500 line of code to work perfectly so I can assist you')
                speak('i am an AI named jarvis made in python by deepak sir, inspired by jarvis AI from the movie iron-man,\
                      i used 15 plus module and 500 plus lines of code to work perfectly so i can assist you')
                speak("what else can i do")
                underline()

            elif 'what can you do' in command:
                speak(TEXT)

            elif 'friend' in command:
                msg = command
                msg = msg.split()
                index = msg.index('friend')
                greet_text = "Hello how are you %s and nice to meet you" % msg[index + 1]
                print(greet_text)
                speak(greet_text)
                speak()
                underline()

            elif 'game' in command:
                # i = random.sample((0, 1), 1)
                i = 0
                if i == 0:
                    game()
                    speak("starting tic-tac-toe")
                else:
                    point, total, incorrect = get_question()
                    print(f'\n\n\tWell Played Your Score is "{point}" out of "{total * 10}"')
                    print(f'\n\tYour incorrect answers are {incorrect}')
                speak("what else can i do")
                underline()

            elif 'help' in command:
                jarvis_help()
                underline()

            elif 'search' in command:
                print("searching...")
                speak("searching")
                query = command.replace('search for', '')
                query = query.strip().capitalize()
                try:
                    print("\nSearching for: ", query)
                    result = wikipedia.summary(query, sentences=5)
                    print(result)
                    speak(result)
                    speak("what else can i do")
                    underline()
                except:
                    print("\nNo Result found! Try on browser!")
                    speak("no Result found, try on browser")
                    result = [];
                    count = 0
                    query = input('\nEnter your search: ')
                    for link in search(query, tld="co.in", num=10, stop=10):
                        webbrowser.open_new_tab(link)
                        count += 1
                        if count == 3:
                            break
                    underline()
                    speak("what else can i do")

            elif 'google' in command:
                result = [];
                count = 0
                txt = command
                query = txt[6:]
                print('Searching for: ', query)
                for link in search(query, tld="co.in", num=10, stop=10):
                    webbrowser.open_new_tab(link)
                    count += 1
                    if count == 3:
                        break
                underline()
                speak("what else can i do")

            elif 'email' in command:
                me = 'dpakverma1234@gmail.com'
                print("Email details?")
                speak("please type email address")
                To = input("Email To: ")
                if To == 'me':
                    To = me
                print("listening Subject")
                speak("tell me Subject")
                Subject = listen()
                underline()
                print("listening messege")
                speak("tell me messege")
                Message = listen()
                email(Message, To, Subject)
                underline()

            elif 'time' in command or 'date' in command:
                time, date, d = time_function()
                print("Current time is: ", time)
                print("Date is:", date)
                speak("Current time is")
                speak(time)
                speak('and todays date is')
                speak(date)
                speak("what else can i do")
                underline()

            elif 'calendar' in command:
                time, date, d = time_function()
                print('This Month or Custom?')
                speak('this month or custom')
                c = listen()
                if 'this month' in c:
                    d = d.split('-')
                    d = [int(x) for x in d]
                    year = d[1]
                    month = d[0]
                if 'custom' in c:
                    print("Which year?")
                    speak('which year')
                    y = listen()
                    year = int(y)
                    print("Which month?")
                    speak('which month')
                    m = listen()
                    month = Month(m)
                cal = calendar.month(year, month)
                speak('here is the calendar')
                print('\n', cal)
                underline()
                speak("what else can i do")

            elif 'calculator' in command:
                speak("opening calculator")
                os.startfile('C:\Windows\System32\calc.exe')
                underline()
                speak("what else can i do")

            elif 'event manager' in command:
                print('What do you want to do AddEvent, ShowEvent, ClearEvent CheckEvent?')
                speak('what do you want to do sir, add event, show event, clear event or check event')
                event = listen()
                if 'add event' in event or 'add' in event:
                    speak('enter number of event to be saved')
                    number_of_event = int(input('Enter number of events to be Saved: '))
                    for i in range(number_of_event):
                        addEvent()
                    print('\nShall I show event?\n')
                    speak('sir do you want to see added event')
                    show = listen()
                    if 'yes' in show:
                        showEvent()
                    if 'no' in show:
                        speak('okay sir')
                if 'show event' in event or 'show' in event:
                    showEvent()
                if 'check event' in event or 'check' in event:
                    checkEvent()
                if 'clear event' in event or 'clear' in event:
                    print("are you sure to clear event?")
                    speak('are you sure to clear event')
                    drop = listen()
                    if 'yes' in drop:
                        clearEvent()
                underline()
                speak("what else can i do!!")

            elif 'shutdown' in command or 'shut down' in command:
                print("are you sure?")
                speak('are you sure')
                drop = listen()
                if 'yes' in drop:
                    speak("initiated shutdown process")
                    os.system("shutdown /s /t 1")
                    break
                else:
                    print("I dropped shutdown process!!")
                    speak("I dropped shutdown process")
                    underline()

            # ************** UNDERDEVELOPMENT************

            elif 'stop' in command or 'stop all process' in command:
                print('Terminating all processes!')
                speak('terminating all process!')
                t1.terminate()
                t2.terminate()
                underline()

            # *********************************************

            else:
                print("I will ask deepak, about this!!")
                speak("I will ask deepak, about this")
                underline()
        except:
            print('Connect me to the internet!!')
            speak('sir connect me to the internet')
            underline()
            out += 1
            if out >= 4:
                print("Due to no internet connection I am turning off!!")
                speak("Due to no internet connection I am turning off")
                underline()
                os._exit(0)
