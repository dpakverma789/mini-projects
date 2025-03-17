#=====MULTI-ALARM==== 

import time
import os
from playsound import playsound
from datetime import datetime
#now=datetime.now()
#current_time=now.strftime("%H:%M")
#print("\nCurrent Time =",current_time,"\n=========")

def alarm(current_time):

    print("\n\nCurrent Time =",current_time,"\n=========")
    
    #(GETTIING NUMBER OF ALARM)
    list=[]
    songList=["\\alarm_clock_2015.mp3"]
    path = os.getcwd()
    index=songList[0]
    song=path+index

    while(True):
        try:
            n=int(input("ENTER NUMBER OF ALARMS: "))
            if n>5:
                print('Only 5 Alarm are Allowed!')
            else:
                print('\n')
                break
        except:
            n=0
            print('ENTER NUMBER OF ALARM FIRST!, THEN I WILL ASK FOR TIME\n')

    #(GETTIING ALRAM TIMINGS)
    for x in range(1,n+1):
          alarm=input("ENTER ALARM TIME: ")
          if alarm >=current_time:
              list.append(alarm)
              list.sort()
          if alarm <=current_time:
              print('REMINDER!, "%s THIS TIME HAS BEEN PASSED, SO I WOULD RING TOMORROW"\n'%(alarm))
              list.append(alarm)
              list.sort()    
              
    msg='ALARM RINGING'
    print("\nYOUR ALARM TIMINGS ARE: ",list)


    #(SETTING UP THE ALARM)
    for i in list:
        if i <=current_time:
            continue
        print("\n\n\nCurrent Time =",current_time,"\n=========")
        hour,mint=i.split(":")                        #TAKING MULTIPLE INPUT SEPERATED BY ":"
        time=hour+":"+mint
        print("\nALARM IS SET FOR =",time,"\n\n\t\t\t\t===YOUR ALARM IS SET===")
        while(True):
            now = datetime.now()
            current_time = now.strftime("%H:%M") #("%H:%M:%S")
            if current_time==time:
                print('\n\t\t\t\t "'+msg.upper()+'"')       
                break
            else:
                continue
        playsound(song)
    print("\n\n\t\t\t\t ===NO MORE ALARMS===")
        
#alarm(current_time)
  
