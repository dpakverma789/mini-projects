

# TIC-TAC-TOW GAME



import random
import time

def randomChoice():
    choice=random.choice([0,1,2,3,4,5,6,7,8])
    return choice 

def displayBoard():

    #============== GAME BOARD====================================
    print("\n**************** NEW GAME ******************")
    print("===GAME BOARD===\n")
    #list=[" "," "," "," "," "," "," "," "," "]
    list=[0,1,2,3,4,5,6,7,8]
    
    print("",list[0],"|",list[1],"|",list[2],"\n",
          "-","+","-","+","-","\n",
          list[3],"|",list[4],"|",list[5],"\n",
          "-","+","-","+","-","\n",
          list[6],"|",list[7],"|",list[8],"\n")

    #====================== GETTING PLAYER NAME===================

    playerOne="YOU"
    playerTwo="AI"

    count=0
    while(True):
        if count==0:
            print("****",playerOne,"'X' v/s",playerTwo,"'O'****")

        #============ GETTING INPUT FROM PLAYER ONE==================
        print("\nBox remaing",9-count)    
        i=int(input("ENTER PLACE YOU WANT TO MARK 'X': "))
       
        while(i>=9):
            print("invalid input!, Enter box number")
            i=int(input("\nENTER PLACE YOU WANT TO MARK 'X': "))
                  
        count+=1
        
        if list[i]==i:
            list[i]="X"                        # (ASSIGNING MARK TO GAME BOARD)
        else:
            while(list[i]!=i):
                print("box already marked")
                i=int(input("\nENTER PLACE YOU WANT TO MARK 'X': "))
            list[i]="X"
       
        print("\n")
        print("",list[0],"|",list[1],"|",list[2],"\n",
        "-","+","-","+","-","\n",
        list[3],"|",list[4],"|",list[5],"\n",
        "-","+","-","+","-","\n",
        list[6],"|",list[7],"|",list[8],"\n")

        #****************** GAME CHECK ****************************
        
        if (list[0]=="X" and list[1]=="X" and list[2]=="X") or (list[0]=="X" and list[3]=="X" and list[6]=="X") :
            print("\n\t\t\t*****",playerOne," are the Winner*****")
            option=input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option=option.upper()
            if option=="Y":
                print("\n\n\n")
                displayBoard()
            else:
                exit()
            
        if (list[3]=="X" and list[4]=="X" and list[5]=="X") or (list[1]=="X" and list[4]=="X" and list[7]=="X"):
            print("\n\t\t\t*****",playerOne," are the Winner*****")
            option=input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option=option.upper()
            if option=="Y":
                print("\n\n\n")
                displayBoard()
            else:
                exit()
        
        if (list[6]=="X" and list[7]=="X" and list[8]=="X") or (list[2]=="X" and list[5]=="X" and list[8]=="X"):
            print("\n\t\t\t*****",playerOne," are the Winner*****")
            option=input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option=option.upper()
            if option=="Y":
                print("\n\n\n")
                displayBoard()
            else:
                exit()
        
        if (list[0]=="X" and list[4]=="X" and list[8]=="X") or (list[2]=="X" and list[4]=="X" and list[6]=="X"):
            print("\n\t\t\t*****",playerOne," are the Winner*****")
            option=input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option=option.upper()
            if option=="Y":
                print("\n\n\n")
                displayBoard()
            else:
                exit()

        #================ CHECKING IS GAME IS TIE OR NOT================
        
        if count==9:
            print("\nBox remaing",9-count) 
            print("\n*****GAME OVER*****\n")
            option=input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option=option.upper()
            if option=="Y":
                print("\n\n\n")
                displayBoard()
            else:
                exit()
            exit()
          
        #======================== PLAYER TWO=====================
        if count<=2:      #Random input 
            choice=randomChoice()
        time.sleep(0.2)
        i=choice
        

        #=========== AI SECTION START ===============
        if count==3:
            if (list[0]=="X" and list[1]=="X"):
                choice=2
                i=choice
            if (list[1]=="X" and list[2]=="X"):
                choice=0
                i=choice
            if (list[0]=="X" and list[2]=="X"):
                choice=1
                i=choice
                
                if list[i]==i:
                    list[i]="O"
                else:
                    index=0
                    while(list[i]!=i):
                        index+=1
                        choice=random.choice([0,1,2])
                        i=choice
                        if index==2:
                            i=random.choice([3,4,5,6,7,8])    
                            
           
            if (list[3]=="X" and list[4]=="X"):
                choice=random.choice([5])
                i=choice
            if (list[4]=="X" and list[5]=="X"):
                choice=random.choice([3])
                i=choice
            if (list[3]=="X" and list[5]=="X"):
                choice=random.choice([4])
                i=choice
                
                if list[i]==i:
                    list[i]="O"
                else:
                    index=0
                    while(list[i]!=i):
                        index+=1
                        choice=random.choice([3,4,5])
                        i=choice
                        if index==2:
                            i=random.choice([0,1,2,6,7,8]) 
                         

            if (list[6]=="X" and list[7]=="X"):
                choice=random.choice([8])
                i=choice
            if (list[7]=="X" and list[8]=="X"):
                choice=random.choice([6])
                i=choice
            if (list[6]=="X" and list[8]=="X"):
                choice=random.choice([7])
                i=choice
                if list[i]==i:
                    list[i]="O"
                else:
                    index=0
                    while(list[i]!=i):
                        index+=1
                        choice=random.choice([6,7,8])
                        i=choice
                        if index==2:
                            i=random.choice([0,1,2,3,4,5]) 
                        

            #VERTICAL CHECK


            if (list[0]=="X" and list[3]=="X"):
                choice=random.choice([6])
                i=choice
            if (list[3]=="X" and list[6]=="X"):
                choice=random.choice([0])
                i=choice
            if (list[0]=="X" and list[6]=="X"):
                choice=random.choice([3])
                i=choice
                
                if list[i]==i:
                    list[i]="O"
                else:
                    index=0
                    while(list[i]!=i):
                        index+=1
                        choice=random.choice([0,3,6])
                        i=choice
                        if index==2:
                            i=random.choice([1,2,4,5,7,8]) 
                         
                   
            if (list[1]=="X" and list[4]=="X"):
                choice=random.choice([7])
                i=choice
            if (list[4]=="X" and list[7]=="X"):
                choice=random.choice([1])
                i=choice
            if(list[1]=="X" and list[7]=="X"):
                choice=random.choice([4])
                
                i=choice
                if list[i]==i:
                    list[i]="O"
                else:
                    index=0
                    while(list[i]!=i):
                        index+=1
                        choice=random.choice([1,4,7])
                        i=choice
                        if index==2:
                            i=random.choice([0,2,3,5,6,8]) 
                         

            if (list[2]=="X" and list[5]=="X"):
                choice=random.choice([8])
                i=choice
            if (list[5]=="X" and list[8]=="X"):
                choice=random.choice([2])
                i=choice
            if (list[2]=="X" and list[8]=="X"):
                choice=random.choice([5])
                i=choice
                
                if list[i]==i:
                    list[i]="O"
                else:
                    index=0
                    while(list[i]!=i):
                        index+=1
                        choice=random.choice([2,5,8])
                        i=choice
                        if index==2:
                            i=random.choice([0,1,3,4,6,7]) 
                        

            #DIAGONAL CHECK
                  # Diagnoal---(0,4,8)
                  
            if (list[0]=="X" and list[4]=="X") or (list[4]=="X" and list[0]=="X"):
                i=8
                if list[i]==i:
                    list[i]="O"
                else:
                    while(list[i]!=i):
                        i=random.choice([1,2,3,5,6,7])
                            
            if (list[4]=="X" and list[8]=="X") or (list[8]=="X" and list[4]=="X"):
                i=0
                if list[i]==i:
                    list[i]="O"
                else:
                    while(list[i]!=i):
                        i=random.choice([1,2,3,5,6,7])
                            
            if (list[0]=="X" and list[8]=="X")or (list[8]=="X" and list[0]=="X"):
                i=4
                if list[i]==i:
                    list[i]="O"
                else:
                    while(list[i]!=i):
                        i=random.choice([1,2,3,5,6,7]) 

                #diaganol--(2,4,6)---         

            if (list[2]=="X" and list[4]=="X") or(list[4]=="X" and list[2]=="X"):
                i=6
                if list[i]==i:
                    list[i]="O"
                else:
                    while(list[i]!=i):
                        i=random.choice([0,1,4,3,5,8,7])
                            
            if (list[4]=="X" and list[6]=="X") or (list[6]=="X" and list[4]=="X"):
                i=2
                if list[i]==i:
                    list[i]="O"
                else:
                    while(list[i]!=i):
                        i=random.choice([0,1,4,3,5,8,7])
                            
            if (list[2]=="X" and list[6]=="X") or (list[6]=="X" and list[2]=="X"):
               i=4
               if list[i]==i:
                   list[i]="O"
               else:
                   while(list[i]!=i):
                       i=random.choice([0,1,4,3,5,8,7])
                            
        #==================AI SECTION END=======================                

        '''******Mark**********'''
        if list[i]==i:
            list[i]="O"
        else:
            while(list[i]!=i):
                choice=randomChoice()
                i=choice
            list[i]="O"
        '''************************'''    
        print("\nBox remaing",9-count)     
        print("Computer played 'O' at:",i)
        count+=1
        print("\n")
        print("",list[0],"|",list[1],"|",list[2],"\n",
        "-","+","-","+","-","\n",
        list[3],"|",list[4],"|",list[5],"\n",
        "-","+","-","+","-","\n",
        list[6],"|",list[7],"|",list[8],"\n")
        
        if (list[0]=="O" and list[1]=="O" and list[2]=="O") or (list[0]=="O" and list[3]=="O" and list[6]=="O") :
            print("\n\t\t\t*****",playerTwo," is Winner*****")
            option=input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option=option.upper()
            if option=="Y":
                print("\n\n\n")
                displayBoard()
            else:
                exit()
            
        if (list[3]=="O" and list[4]=="O" and list[5]=="O") or (list[1]=="O" and list[4]=="O" and list[7]=="O"):
            print("\n\t\t\t*****",playerTwo," is Winner*****")
            option=input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option=option.upper()
            if option=="Y":
                print("\n\n\n")
                displayBoard()
            else:
                exit()
        
        if (list[6]=="O" and list[7]=="O" and list[8]=="O") or (list[2]=="O" and list[5]=="O" and list[8]=="O"):
            print("\n\t\t\t*****",playerTwo," is Winner*****")
            option=input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option=option.upper()
            if option=="Y":
                print("\n\n\n")
                displayBoard()
            else:
                exit()
        
        if (list[0]=="O" and list[4]=="O" and list[8]=="O") or (list[2]=="O" and list[4]=="O" and list[6]=="O"):
            print("\n\t\t\t*****",playerTwo," is Winner*****")
            option=input("\nWANT TO PLAY NEW GAME? Y/N: ")
            option=option.upper()
            if option=="Y":
                print("\n\n\n")
                displayBoard()
            else:
                exit()

#Main Function
def main():
    displayBoard()
    
if (__name__ == "__main__"):
    main()

