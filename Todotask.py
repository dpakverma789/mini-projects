
#import os
import time
import os
from playsound import playsound
from datetime import datetime

#DATE FUNCTION
now = datetime.now()
current_time = now.strftime("%H:%M") #("%H:%M:%S")
print("\nCurrent Time =",current_time,"\n=========")

#CREATING TASK LIST
def CreateTask():
    list=[]
    #fileName=input("Enter file name to be created ")    #getting file name from user
    #fileName=fileName+"."+"txt"
    file=open("E:\Task.txt",'a+')            #creating the new file named new in write mode
    num=int(input("Enter number of task :"))
    count=1
    while(count<=num):
        msg=input("Enter Task: ")
        time=input("Enter Task Reminder time: ")
        msg=msg.strip()
        msg=msg+" - "
        file.write(msg)
        file.write(time)
        file.write("\n")
        count+=1
    return    
    
    
#READING TASK LIST
def ReadTask():
    try:
        print('\n')
        count=1
        file=open("E:\Task.txt","r+")
        print("To do List is: \n")
        count=1
        for i in file:
            print(count,"",i.upper())
            x=i.find("-")
            count+=1
        file.close()
        if count==1:
            print("\t\t***********To do List is EMPTY***********")
        return 
    except:
        print("\t\t***********File Not Found***********")
        


#DELETING FILE
def fileDelete():
    try:
        os.remove("E:\Task.txt")
        print("File Deleted")
    except:
        print("\n\n\t\t***********File Not Found***********")


#DELETING FILE DATA
def clearFile():
    file=open("E:\Task.txt","w")
    file.truncate()
    print("\n\n\t\t***********File Data Removed***********")

    
#MAIN FUCNTION   
text="TO DO LIST"
if __name__=="__main__":
    print("\n")
    print("\t"*3,text)
    print("\nPRESS 1 FOR CreateTask \t\t PRESS 2 FOR ReadTask")
    print("\nPRESS 3 FOR Exit \t\t PRESS 4 DELETE To Do list file")
    print("\nPRESS 5 FOR Clear List data \t UnderDevelopment ")
    choice=int(input("\nENTER YOUR CHOICE HERE :"))
    if choice ==1:
        lst=CreateTask()
        print("Task Updated")
        exit()
    if choice ==2:
        task=ReadTask()
    if choice==3:
        exit()
    if choice==4:
        delete=fileDelete()
    if choice==5:
        clear=clearFile()      


