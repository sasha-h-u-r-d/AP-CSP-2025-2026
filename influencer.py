#Sasha Hurd-Groves
#influencer.py
import pandas as pd

influencer=pd.read_csv("influencer.csv")
month=influencer["Month"].tolist()
view=influencer["Views"].tolist()
dislike=influencer["Dislikes"].tolist()
subscribe=influencer["Subscriber(+-)"].tolist()
revenue=influencer["Revenue"].tolist()

def golden(sub):
    subs=[]
    for i in range(len(influencer)):
        if subscribe[i]>=sub:
            subs.append(influencer.loc[i])
            i=i+1
        else:
            i=i+1
    print(subs)
golden(50000)
def humble(viewers):
    views=[]
    for i in range(len(influencer)):
        if view[i]<=viewers:
            views.append(influencer.loc[i])
            i=i+1
        else:
            i=i+1
    print(views)
humble(2000)
def scandal(oh_no):
    whoops=[]
    for i in range(len(influencer)):
        if revenue[i]==oh_no:
            whoops.append(influencer.loc[i])
            i=i+1
        else:
            i=i+1
    print(whoops)
scandal(0)
