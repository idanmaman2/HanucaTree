
import random 
import time 


class bcolors:
    YELLOW='\033[33m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

H = 200

def changecolorRand():
    print(random.choice([bcolors.HEADER,bcolors.OKBLUE,bcolors.OKCYAN,bcolors.OKGREEN,bcolors.FAIL,bcolors.ENDC]),end="")





print("\x1b[2J");
while(True):
    print("\x1b[H"); 
    time.sleep(random.random())
    print(bcolors.YELLOW,end="")
    print(*[("*"*i).center(H-1) for i in range(1,H//10,5)],sep="\n",end="\n")
    print(*[("*"*i).center(H-1) for i in range(H//10,1,-5)],sep="\n",end="")  
    for i in range(1,H,2):
        for j in range(((H-1)-i)//2):
            print(" ",end="")
        for j in range(i):
            if(random.randint(0,2) == 0 ):
                changecolorRand()
            else : 
                print(bcolors.OKGREEN,end="")
            print("*",end="")
        for j in range(((H-1)-i)//2):
            print(" ",end="")
        print(end="\n")
    print(bcolors.FAIL,end="")
    for i in range(H//5):
        print((("*")*(H//4)).center(H-1))
    print(bcolors.OKBLUE)
    print(*("#"*H for i in range(H//10)),sep="\n")
    
   
    

    