#Sasha Hurd
#guest.py
#You are hosting a party and have created an array to store all of the guests coming to the event.


guests = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Kevin", "Liam", "Mallory", "Nia", "Oscar",
"Peggy", "Quinn", "Riley", "Sybil", "Trent", "Uma", "Victor", "Walter", "Xander", "Yara", "Zane", "Amari", "Blake", "Casey", "Dakota"]

print(len)
Bob=input("Who is your plus one?: ")
guests.append(Bob)
VIP=input("Who is the VIP?: ")
guests.insert(0,VIP)
new=input("Who is the new guest?: ")
guests.remove("David")
guests.insert(4, new)
print(guests)
print(len(guests))

