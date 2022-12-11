
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
    
    
    for i in range(1,H//20,4):
        changecolorRand()
        print(("*" * i).center(H-3))
    for i in range(H//20,1,-4):
        changecolorRand()
        print(("*" * i).center(H-3))
    
    
    time.sleep(random.random())
    for i in range(1,H//20,3):
        print(" "*(H//36),end="")
        for j in range(4):
            changecolorRand()
            print(("*" * i).center(H//18),end=" "*(H//18))
        print(bcolors.YELLOW,end="")
        print("*" *  (H//18),end=" "*(H//18))
        for j in range(4):
            changecolorRand()
            print(("*" * i).center(H//18),end=" "*(H//18))
        print(end="\n")
        
        
    for i in range(H//20,1,-3):
        print(" "*(H//36),end="")
        for j in range(4):
            changecolorRand()
            print(("*" * i).center(H//18),end=" "*(H//18))
        print(bcolors.YELLOW,end="")
        print("*" * (H//18),end=" "*(H//18))
        for j in range(4):
            changecolorRand()
            print(("*" * i).center(H//18),end=" "*(H//18))
        print(end="\n")
        
        
    print(bcolors.YELLOW,end="")
    for i in range(9):
        for j in range(3): 
            if i%2 : 
                print((" "*(H//18)).join(["*"*(H//18) for i in range(9-i)]).center(H))
            else : 
             print(("*" * (H - H//9 * i)).center(H) )
    for i in range(H//9):
      print((("*")*(H//9)).center(H-1))
        
