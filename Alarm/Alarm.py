# ===== Multi- Alarm Script ====

import random
import os
from datetime import datetime
try:
    from playsound import playsound
except ModuleNotFoundError:
    os.system('pip install playsound')
    from playsound import playsound


now = datetime.now()
time = now.strftime("%H:%M")


def alarm(current_time):
    print("\n\nCurrent Time =", current_time, "\n=========")

    # GETTING NUMBER OF ALARM
    alarm_container = []
    alarm_ringtones = os.listdir('ringtones')
    ringtone_index_pointer = random.randint(0, len(alarm_ringtones)-1)
    ringtone = os.path.join(os.path.abspath('ringtones'), alarm_ringtones[ringtone_index_pointer])

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
            print('REMINDER!, "%s THIS TIME HAS BEEN PASSED, SO I WOULD RING TOMORROW"\n' % alarm_timing)
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
