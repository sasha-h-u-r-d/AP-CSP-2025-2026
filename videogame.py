#Sasha Hurd-Groves
#videogame.py

#Imports
import pandas as pd

#Function
global level
data=pd.read_csv("gamedev.csv")
level=data["Level"].tolist()
time=data["Time"].tolist()
rating=data["Rating"].tolist()
feedback=data["Feedback"].tolist()

def redflag(rate):
    rates=[]
    for i in range(len(data)):
        if rating[i]<=rate:
            rates.append(data.loc[i])
            i=i+1
        else:
            i=i+1
    print(rates)
def timer(times,rate):
    this_one=[]
    for i in range(len(data)):
        if time[i]>=times and rating[i]>=rate:
            this_one.append(data.loc[i])
            i=i+1
        else:
            i=i+1
    print(this_one)
def secret(word):
    secretive=[]
    for i in range(len(data)):
        if word in feedback[i]:
            secretive.append(data.loc[i])
            i=i+1
        else:
            i=i+1
    print(secretive)
secret("secret")
timer(100,3)
redflag(3)
