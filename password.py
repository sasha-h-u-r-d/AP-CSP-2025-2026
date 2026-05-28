#password
#Sasha Hurd
#Write a program that keeps asking for a password until the user types “python”.

#Function
def main():
    while True:
        pswrd=input("Password= ")
        if pswrd != "python":
            print ("Incorrect! Try Again")
            continue
        elif pswrd == "python":
            print("Access Granted!")
            break






#Main
main()
