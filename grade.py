#Sasha
#grade
#Write a function that asks the user to input a score as an integer and returns the appropriate letter grade


def grade():
    l= int(input("please write your score as an integer"))
    if l>=90:
        print ("A")
    elif l>=80:
        print ("B")
    elif l>=70:
        print ("C")
    elif l>=60:
        print ("D")
    else:
        print ("F")

grade()
