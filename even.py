#Even
#Sasha Hurd
#Create a program that takes in a number and prints all even numbers from 2 up to that number. This reinforces loops and counting patterns.

#Function
def main():
    number=input("Please type in a number")
    for i in range (2, int(number)+2, 2):
        print (i)


#Main
main()
