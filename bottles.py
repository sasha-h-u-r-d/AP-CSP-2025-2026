#Sasha Hurd
#Create a Python program that generates and prints out the lyrics to the song "99 Bottles of Milk on the Wall." Follow the guidelines below:

#Instructions:

#Utilize a loop to iterate through the verses of the song.
#Use variables to store the current number of bottles and update them within the loop.
#Refrain from manually typing in the numbers in the lyrics.
#Ensure that when there is only 1 bottle left, the word "bottles" becomes singular.

#Function
def main(x):
    for i in range(x):
        print(x,"bottles of milk on the wall, ",x,"bottles of milk.")
        x=x-1
        print("Take one down and pass it around,",x,"bottle of milk on the wall.")
        if x<=1:
            print(x,"bottle of milk on the wall,",x,"bottle of milk.")
            break
    print("Take it down pass it around")
    print("No more bottles of milk on the wall.")
    print("Boo Hoo!")
#Main
main(99)

