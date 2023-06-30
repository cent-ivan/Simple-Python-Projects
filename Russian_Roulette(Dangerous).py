import os
import random

gun = [0,0,0,0,0,1]

chamber = random.choice(gun)

if chamber == 0:
    print("Phewwww")
else:
    os.remove("Bang") #C:\Windows\System32