#hogwarts.py
#SashaHurd
#Create a Python program that asks the user for their and assigns them to one of the from the series.

#Init
import time
import random
#Functions

def main():
    print("Welcome to Hogwarts")
    name=input("Please Enter Your Name: ")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print(".....")
    time.sleep(1)
    print(house(name))

def house(name):
    if name == "harry" or name == "hermione" or name == "ron":
        return "Gryffindor"
    elif name == "newt" or name == "nymphadora" or name == "pomona":
        return "Hufflepuff"
    elif name == "luna" or name == "cho" or name == "filius":
        return "Ravenclaw"
    elif name == "draco" or name == "voldemort" or name == "severus":
        return "Slytherin"
    else:
        rand_house = random.randint(1,4)
        if rand_house == 1:
            return "Gryffindor"
        elif rand_house == 2:
            return "Hufflepuff"
        elif rand_house == 3:
            return "Ravenclaw"
        else:
            return "Slytherin"

main()



