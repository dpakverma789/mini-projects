# ===== Multi- Alarm Script ====
import random
from datetime import datetime
import os
import sys
PROJECT_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
REQUIREMENTS_FILE = os.path.join(PROJECT_DIRECTORY,'requirements.txt')
RING_DIRECTORY = os.path.join(PROJECT_DIRECTORY, 'ringtones')
root_dir = os.path.dirname(PROJECT_DIRECTORY)
sys.path.insert(0, root_dir)

def install_requirements(file=None):
    return os.system(f'pip install -r {file}')

def remove_requirements(file=None):
    if os.path.isfile(file):
        return os.system(f'pip uninstall -y -r {file}')
    return False

try:
    from playsound import playsound
except ModuleNotFoundError:
    try:
        if not os.path.isfile(REQUIREMENTS_FILE):
            raise FileNotFoundError
        install_requirements(REQUIREMENTS_FILE)
    except FileNotFoundError:
        os.system('python -m pip install --upgrade pip')
        for pack in ('playsound',):
            os.system(f'pip install {pack}')
        from playsound import playsound
    finally:
        os.system('pip freeze > requirements.txt')

now = datetime.now()
time = now.strftime("%H:%M")


def alarm(current_time):
    print("\n\nCurrent Time =", current_time)
    print("Enter Time in { HH:MM } 24HR formate like", current_time, "\n=========")

    # GETTING NUMBER OF ALARM
    alarm_container = []
    alarm_ringtones = os.listdir(RING_DIRECTORY)
    ringtone_index_pointer = random.randint(0, len(alarm_ringtones)-1)
    ringtone = os.path.join(RING_DIRECTORY, alarm_ringtones[ringtone_index_pointer])

    while True:
        try:
            n = int(input("ENTER NUMBER OF ALARMS: "))
            if n > 5:
                print('Only 5 Alarm are Allowed!')
            else:
                print('\n')
                break
        except ValueError:
            n = 0
            print('ENTER NUMBER OF ALARM FIRST!, THEN I WILL ASK FOR TIME\n')

    # GETTING ALARM TIMINGS
    for x in range(1, n + 1):
        alarm_timing = input("ENTER ALARM TIME: ")
        if alarm_timing > current_time:
            alarm_container.append(alarm_timing)
            alarm_container.sort()
        if alarm_timing <= current_time:
            print('REMINDER!, "%s THIS TIME HAS BEEN PASSED, SO IT WOULD RING TOMORROW"\n' % alarm_timing)
            alarm_container.append(alarm_timing)
            alarm_container.sort()

    msg = 'ALARM RINGING'
    print("\nYOUR ALARM TIMINGS ARE: ", alarm_container)

    # SETTING UP THE ALARM
    for i in alarm_container:
        if i <= current_time:
            continue
        print("\n\n\nCurrent Time =", current_time, "\n=========")
        hour, mint = i.split(":")  # TAKING MULTIPLE INPUT separated BY ":"
        alarm_set_time = hour + ":" + mint
        print("\nNext Alarm: ", alarm_set_time, "\n\n\t\t\t\t===YOUR ALARM IS SET===")
        while True:
            time_now = datetime.now()
            current_time = time_now.strftime("%H:%M")  # ("%H:%M:%S")
            if current_time == alarm_set_time:
                print('\n\t\t\t\t "' + msg.upper() + '"')
                break
            else:
                continue
        for _ in range(3):
            playsound(ringtone)
    print("\n\n\t\t\t\t ===NO MORE ALARMS===")


if __name__ == "__main__":
    alarm(time)
