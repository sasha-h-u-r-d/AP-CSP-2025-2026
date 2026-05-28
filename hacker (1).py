#Sasha Hurd-Groves
#hacker.py
import pandas as pd

hacker=pd.read_csv("hacker.csv")
Log=hacker["Log_ID"].tolist()
Addy=hacker["IP_Address"].tolist()
Proto=hacker["Protocol"].tolist()
Data=hacker["Data_KB"].tolist()
Time=hacker["Time"].tolist()
Desc=hacker["Description"].tolist()


def login(word):
    log=[]
    for i in range(len(hacker)):
        if word in Desc[i]:
            log.append(Desc[i])
    print(log)
login("Login Success")

def transfer(word):
    bulk=[]
    for i in range(len(hacker)):
        if word in Desc[i]:
            bulk.append(hacker.loc[i])
    print(bulk)
transfer("Bulk")
def reset(word):
    pswd=[]
    for i in range(len(hacker)):
        if word in Desc[i]:
            pswd.append(Desc[i])
    print(len(pswd))
reset("Reset")
