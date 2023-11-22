import os
import sys
import random


#global values for the system
ANSWERS = ["ALOFT","BIRTH","CHAOS","DRANK","EMPTY","FOUND"]
TERMINAL = False

guess = input("Find the 5 letter word in 6 guesses or less")
cap_guess = guess.upper()

answer = ANSWERS[random.randint(0,len(ANSWERS)-1)]


"""detects if we are in the IDLE shell or not"""
try:
    TERMINAL = False
    color = sys.stdout.shell
except AttributeError:
    TERMINAL = True

def clear_screen():
    """Clears the console screen"""
    if(os.name=="posix"):  #linux
        os.system("clear")
    else:
        os.system("cls")    #windows

#draw color
def print_green(msg):
    """Prints in green, no newline"""
    if(TERMINAL):
        print("\033[1m\033[92m {}\033[00m" .format(msg),end="")
    else:
        color.write(" {} " .format(msg),"STRING")

def print_yellow(msg):
    """Prints in yellow, no newline"""
    if(TERMINAL):
        print("\033[1m\033[93m {}\033[00m" .format(msg),end="")
    else:
        color.write(" {} " .format(msg),"KEYWORD")

def print_normal(msg):
    """Prints normal, no newline"""
    if(TERMINAL):
        print("\033[96m {}\033[00m" .format(msg),end="")
    else:
        print(" {} " .format(msg),end="")

def duplicate_letter(upper_guess):
    while(len(upper_guess)==5):
        count = 0
        for j in range (5):
            for i in range (j+1,5):
                if(upper_guess[j] == upper_guess[i]):
                    count+=1
        if(count == 0):
            return True
        return False
    if (len(upper_guess)!=5):
        return False

guess = []
def previous_guess(upper_guess,guess):
    if(duplicate_letter(upper_guess)== True):
        for i in range(len(guess)):
            if(upper_guess == guess[i]):
                return True
        return False
    return True
            

def good_guess(upper_guess,guess):
    if(previous_guess(upper_guess,guess) == True):
        return "Not a good guess. Try again"
    else:
        guess += [upper_guess]
        return upper_guess

count = 1
while(count < 7):
    if(cap_guess == good_guess(cap_guess,guess)):
        count+=1
        for i in range (len(cap_guess)):
            if(cap_guess[i] == answer[i]):
                print_green(cap_guess[i])
            elif(cap_guess[i] in answer):
                print_yellow(cap_guess[i])
            else:
                print_normal(cap_guess[i])
    else:
        print("Not a good guess. Try again")
    if(cap_guess == answer):
        print("\nYou won!!!")
        break
    if(count < 7):
        user_guess = input("\n")
        cap_guess = user_guess.upper()

if(count == 7):
    print("\nMaybe better luck next time!")
input("please press enter to exit")
    
    

       
   
      
            
        
       
