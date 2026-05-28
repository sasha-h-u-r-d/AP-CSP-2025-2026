#Sasha Hurd-Groves
#simulation.py
#Import
import random

#Initialize Conditions
tortoise=[]
hare=[]
for i in range(100000):
    finish_line = 50
    tortoise_pos = 0
    hare_pos = 0
    is_hare_asleep = False
    while tortoise_pos < finish_line and hare_pos < finish_line:
        tortoise_pos = tortoise_pos + random.randint(1,3)
        sleep = random.randint(1,10)
        if sleep < 4:
            is_hare_asleep = True
        else:
            is_hare_asleep = False
        if is_hare_asleep == False:
            hare_pos = hare_pos + random.randint(1,10)
        elif is_hare_asleep == True:
            hare_pos = hare_pos + 0
    if tortoise_pos >= 50:
        tortoise.append("win")
    else:
        hare.append("win")
if len(tortoise) > len(hare):
        print("🐢 Tortoise won more at", len(tortoise) ,"rounds")
elif len(hare) > len(tortoise):
        print("🐇 Hare won more at", len(hare) ,"rounds")
