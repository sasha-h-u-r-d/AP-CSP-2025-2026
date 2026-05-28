#Sasha Hurd
#To practice working with global variables and conditional statements in Python, specifically for challenge 3 by building a program called Pokemon Evolution

count=0

#Functions
def points():
    global count
    count=count + 100
    print("Score is now",count)

points()
points()
points()
