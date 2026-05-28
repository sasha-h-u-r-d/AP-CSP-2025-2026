#Sasha Hurd
#This program defines a function 3 functions that simulate transactions in an atm

#Initialize
balance = 500

#Function
def func():
    print("You currently have",balance,"dollars in your account")
    what=(input("Would you like to deposit, withdraw, or see your balance?"))
    if what=="deposit":
        deposit()
    elif what=="withdraw":
        withdraw()
    elif what=="see my balance":
        total()
    else:
        print("Please choose an option")
def deposit():
    global balance
    y=(int(input("How much money would you like to deposit? ")))
    balance=balance + y
    print("You now have",balance,"dollars in your account")

def withdraw():
    global balance
    x=(int(input("How much money would you like to withdraw? ")))
    if balance-x<0:
        print("I'm sorry you cannot withdraw as you do not have enough money")
    else:
        balance=balance - x
        print("You now have",balance,"dollars in your account")

def total():
    global balance
    print(balance)
func()
