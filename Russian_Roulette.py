#import os
import random

def shootGun():
    gun = [0,0,0,0,0,1]

    chamber = random.choice(gun)

    if chamber == 0:
        print("Phewwww")
    else:
        print("Bang") #C:\Windows\System32

def action():
    print("Press 's' to load the gun and test your luck")
    try:
        move = input(">>> ")
    except ValueError:
        print("Inavlid Value")
        action()

    if move == "s":
        shootGun()
    else:
        print("Invalid Command")
        action()

action()