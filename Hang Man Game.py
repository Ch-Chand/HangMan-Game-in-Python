from time import sleep
import random
from os import system
def Clear():
    _=system('cls')
def Word():
    a=random.randrange(1, 6)
    return words[a]
def Loader():
    print("               ", end="")
    for i in range(0,25):
        print("#", end="")
        sleep(0.18)
    print("\n")
words={1:'america',2:'pakistan',3:'india',4:'bangladesh',5:'indonesia'}
w=Word()
char=list(w)
size=len(w)
user_enter=[]
chances=3
for i in range(0,size):
    user_enter.append('__')
#Loader()
sleep(0.2)
Clear()
print("                  Welcome To Hangman")
print("Total lives are ", chances)
print("Length of Guessing word is ",size)
for j in range(0, size):
    print(user_enter[j], end=" ")
for i in range(1,size+chances):
    if chances>=1:
        a=input()
        Clear()
        if a in char:
            user_enter[char.index(a)]=a
            char[char.index(a)]=-1
        else:
            chances=chances-1
    else:
        print("\nSorry! Try Again")
        break
    print("Life ", chances, "\n")
    for j in range(0, size):
        print(user_enter[j], end=" ")
    if '__' not in user_enter:
        print("\n\"",w,"\"\nYou Nailed it, WelDone")
        break