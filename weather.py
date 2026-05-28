#Sasha
#weather.py
#Create a program that advises you on what clothing to wear and accessories to bring based on temperature given.

#Function
def clothing():
    temp=int(input("please put in the temperature"))
    if temp>=90:
        print("wear short sleeves and shorts with bathing suits")
    elif temp>=70:
        print("wear light pants and short sleeves or swap")
    elif temp>=40:
        print("wear coats and warm clothing")
    elif temp>=0:
        print("wear thick clothes and plenty of warm accessories")






#Main
clothing()
