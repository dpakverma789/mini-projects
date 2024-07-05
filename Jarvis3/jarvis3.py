# Built-In Libraries
import os
import random
from datetime import datetime
os.chdir('F:\python_programs\Jarvis3')
import re
try:
    # Importing Module
    import pyttsx3
    import webbrowser
    import speech_recognition as sr
    from playsound import playsound
    import wikipedia
    from googlesearch import search
    from email.mime.text import MIMEText
    import pygame
    # User-Define Libraries
    # from Month import *
    # from TicTac_AI import *
    from Event_Manager.EventManager import *
    # from alarm import *
    # from quiz_Game import get_question
except ModuleNotFoundError:
    with open(os.path.join(os.getcwd(), 'requirements.txt')) as file:
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
    # from Month import *
    # from TicTac_AI import *
    from Event_Manager.EventManager import *
    # from alarm import *
    # from quiz_Game import get_question


class JARVIS2:
    # Class Variable
    JARVIS_GREET_RESPONSE = ('how are you', 'hows going on', 'hows your day going')
    SPEECH_ENGINE = pyttsx3.init('sapi5')
    pygame.init()

    def __init__(self, VOICE_TOKEN, MAX_NUMBER_OF_ATTEMPTS):
        self.VOICE_TOKEN = VOICE_TOKEN
        self.MAX_NUMBER_OF_ATTEMPTS = MAX_NUMBER_OF_ATTEMPTS

    def jarvis_listening(self) -> str:
        is_jarvis_listing = True
        number_of_listening_attempts = 0
        microphone = sr.Recognizer()
        microphone.energy_threshold = 3500
        microphone.pause_threshold = 1
        with sr.Microphone() as source:
            while is_jarvis_listing:
                command = None
                number_of_listening_attempts += 1
                print("I am Listening...")
                self.jarvis_speak(COMMAND="I am Listening")
                audio = microphone.listen(source)
                print("Give me a Moment!!")
                self.jarvis_speak(COMMAND="give me a moment")
                try:
                    command = microphone.recognize_google(audio, language="en-in")
                    print("You said : %s!\n" % command)
                    command = command.lower()
                except sr.UnknownValueError:
                    print("Could not understand please say it again!!")
                    self.console_formator()
                    self.jarvis_speak(COMMAND="Could not understand please say it again")
                else:
                    is_jarvis_listing = False
                if number_of_listening_attempts == self.MAX_NUMBER_OF_ATTEMPTS and not command:
                    print("Due to no response I am turning Off!!")
                    self.jarvis_speak(COMMAND="due to no response i am turning off")
                    os._exit(0)
        return command

    def jarvis_speak(self, COMMAND: str) -> None:
        JARVIS3.SPEECH_ENGINE.setProperty('rate', 175)
        JARVIS3.SPEECH_ENGINE.setProperty('voice', self.VOICE_TOKEN)
        JARVIS3.SPEECH_ENGINE.say(COMMAND)
        JARVIS3.SPEECH_ENGINE.runAndWait()
        return

    def console_formator(self) -> None:
        print("------"*5, '\n')
        return

    def time_function(self) -> str:
        now = datetime.now()
        return now.strftime("%I:%M:%p"), now.strftime("%A %d-%B-%Y")

    def jarvis_greetings(self) -> None:
        current_time, today_day_date = jarvis_task.time_function()
        current_hour, current_min, current_phase = current_time.split(':')
        if '12' > current_hour and current_phase == 'AM':
            jarvis_task.jarvis_speak(COMMAND='good morning')
        elif '04' > current_hour and current_phase == 'PM':
            jarvis_task.jarvis_speak(COMMAND='good afternoon')
        else:
            jarvis_task.jarvis_speak(COMMAND='good evening')
        jarvis_task.jarvis_speak(COMMAND=random.choice(JARVIS2.JARVIS_GREET_RESPONSE))
        return


class JARVIS3(JARVIS2):
    # Class Variable
    TIMER = 30
    ZIRA = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0"
    DAVID = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0"
    MUSIC_CATEGORY = ('D:\\Music\\Coders', 'D:\\Music\\High Notes', 'D:\\Music\\Low Notes')
    START_NOTE = ('\nI CAN PLAY MUSIC, SET ALARM, BROWSE WIKIPEDIA, BROWSE GOOGLE,'
                  ' BROWSE YOUTUBE OPEN BROWSER, SEND EMAIL SHOW DATE-TIME, CALENDAR, OPEN CALCULATOR,'
                  ' PLAY GAME, HANDLE EVENT MANAGER AND SHUTDOWN SYSTEM'
                  '\n\n(Say "do nothing" to put me on wait for few minute)\n')
    INTRODUCTION = 'sir jarvis at your service any task for me'

    def __init__(self, VOICE_TOKEN, MAX_NUMBER_OF_ATTEMPTS):
        super().__init__(VOICE_TOKEN, MAX_NUMBER_OF_ATTEMPTS)

    def jarvis_change_voice(self) -> bool:
        self.VOICE_TOKEN = JARVIS3.ZIRA if self.VOICE_TOKEN == JARVIS3.DAVID else JARVIS3.DAVID
        return True

    def jarvis_music_control(self) -> object:
        music_directory = random.choice(self.MUSIC_CATEGORY)
        music_list = os.listdir(music_directory)
        random.shuffle(music_list)
        music_name = random.choice(music_list)
        try:
            music_path = os.path.join(music_directory, music_name)
            soundtrack = pygame.mixer.Sound(music_path)
            soundtrack.play()
            return soundtrack
        except:
            self.jarvis_music_control()


if __name__ == "__main__":
    is_jarvis_alive = True
    jarvis_task = JARVIS3(VOICE_TOKEN=JARVIS3.DAVID, MAX_NUMBER_OF_ATTEMPTS=3)
    jarvis_task.jarvis_greetings()
    jarvis_task.jarvis_speak(COMMAND=JARVIS3.INTRODUCTION)
    checkEvent()
    print('\n')
    while is_jarvis_alive:
        command = jarvis_task.jarvis_listening()
        if re.search(r'\b(play music|play the song|change the song|change music)\b', command, re.IGNORECASE):
            try:
                music.stop()
                jarvis_task.jarvis_speak(COMMAND='playing music, enjoy the track')
                music = jarvis_task.jarvis_music_control()
            except:
                music = jarvis_task.jarvis_music_control()
        elif re.search(r'\b(stop the music|stop the song|stop music)\b', command, re.IGNORECASE):
            music.stop()
        elif re.search(r'\b(event manager)\b', command, re.IGNORECASE):
            music.stop()
        elif re.search(r'\b(change your voice|voice)\b', command, re.IGNORECASE):
            jarvis_task.jarvis_change_voice()
        elif re.search(r'\b(do nothing|go to sleep|keep quite|nothing)\b', command, re.IGNORECASE):
            jarvis_task.jarvis_speak(COMMAND='taking short break')
            print('I WILL BE RIGHT BACK in %s sec' % JARVIS3.TIMER)
            if JARVIS3.TIMER == 30:
                sleep(JARVIS3.TIMER)
            else:
                sleep(JARVIS3.TIMER)
                JARVIS3.TIMER = 30
                jarvis_task.console_formator()
                continue
            JARVIS3.TIMER += 30
            jarvis_task.console_formator()
        elif re.search(r'\b(bye|good bye|goodbye)\b', command, re.IGNORECASE):
            jarvis_task.jarvis_speak(COMMAND='good bye sir')
            os._exit(0)