#Search.py
#Sasha Hurd-Groves

import random

def search():
    attempts=0
    secret_number=random.randint(1,100)
    for guess in range(1,101):
        if guess == secret_number:
            print(f"Attempts: {attempts}")
            break

        else:
            attempts=attempts+1
            continue
def binary_search():
    low=1
    high=100
    attempts=0
    secret_number=random.randint(1,100)
    found=False
    while found==False:
        mid=(high+low)//2
        if secret_number==mid:
            attempts=attempts+1
            print(f"Attempts: {attempts}")
            found=True
        elif mid<secret_number:
            low=mid+1
            attempts=attempts+1
        elif mid>secret_number:
            high=mid-1
            attempts=attempts+1

binary_search()


