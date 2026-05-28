#Sasha Hurd-Groves
#dog_breeds.py

import pandas as pd
import webbrowser
import time

dog=pd.read_csv("dogs.csv")
ID=dog["id"].tolist()
name=dog["Name"].tolist()
breed=dog["Breed Group"].tolist()
bred=dog["BredFor"].tolist()
min=dog["Minimum Life Span"].tolist()
max=dog["Maximum Life Span"].tolist()
min_height=dog["Minimum Height"].tolist()
max_height=dog["Maximum Height"].tolist()
min_weight=dog["Minimum Weight"].tolist()
max_weight=dog["Maximum Weight"].tolist()
temp=dog["Temperament"].tolist()
image=dog["Image"].tolist()

def getDogSize(size):
    if size == "tiny":
        dogs=[]
        for i in range(len(min_weight)):
            if min_weight[i]<=10:
                dogs.append(name[i])
        print("Recommended dogs = ",dogs)
        dogs.clear()
    elif size == "small":
        dogs=[]
        for i in range(len(min_weight)):
            if min_weight[i]<=25 and min_weight[i]>=11:
                dogs.append(name[i])
        print("Recommended dogs = ",dogs)
        dogs.clear()
    elif size == "medium":
        dogs=[]
        for i in range(len(min_weight)):
            if min_weight[i] <= 60 and min_weight[i]>=26:
                dogs.append(name[i])
        print("Recommended dogs = ",dogs)
        dogs.clear()
    elif size == "large":
        dogs=[]
        for i in range(len(min_weight)):
            if min_weight[i] >= 60:
                dogs.append(name[i])
    else:
        print("Size not found, please input a legitimate size.")



def findDogBreed(breed_name):
    if breed_name in name:
        for i in range(len(temp)):
            if breed_name == name[i]:
                print("Your dog's temperament is ", temp[i])
                webbrowser.open(image[i])
    else:
        print("Dog not found in list, please input a different dog.")


def findDogUse(purpose):
    dogs=[]
    for i in range(len(bred)):
        if purpose in bred[i]:
            dogs.append(name[i])

    if (len(dogs)) == 0:
        print("I'm sorry that purpose is not included.")
    else:
        print("Dogs that match your purpose are ", dogs)
    dogs.clear()





def menu():
        print("I heard someone is looking for their new best friend!")
        time.sleep(1)
        while True:
            choice=input("Would you like to find information about the dog's weight, temper, breed for a purpose, or exit? ")
            if choice.lower() == "dog's weight":
                print("..............")
                time.sleep(1)
                weight=input("What is the size dog you would like (tiny, small, medium, or large)? ")
                print("..............")
                time.sleep(1)
                if weight.lower() == "tiny":
                    getDogSize("tiny")
                elif weight.lower() == "small":
                    getDogSize("small")
                elif weight.lower() == "medium":
                    getDogSize("medium")
                elif weight.lower() == "large":
                    getDogSize("large")
            elif choice.lower() == "temper":
                print("..............")
                time.sleep(1)
                dog=input("What is your dog breed's name? " )
                findDogBreed(dog)
            elif choice.lower() == "breed for a purpose":
                print("..............")
                time.sleep(1)
                purps=input("What is your wanted purpose? ")
                purps=purps.capitalize()
                findDogUse(purps)
                continue
            elif choice.lower() == "exit":
                print("I hope you find your forever friend!")
                break


menu()

Dataset Source Information:
#Dog Dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source:https://thedogapi.com/en
Deliverable: .py file
