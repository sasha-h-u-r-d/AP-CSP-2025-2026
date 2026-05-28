#to-do.py
#Sasha Hurd
# The program should utilize lists in Python to store and manipulate the tasks. By completing this assignment, you will strengthen your understanding of lists, user input, and basic control structures in Python.

#Init
#Function
def lists():
    x=1
    list=["S","N"]
    done=["A"]
    while x>0:
        print("Current list: ",list)
        do=input("Would you like to remove, add, or relabel an item as finished?: ")
        do=do.lower()
        if do=="add":
            print("Current list: ",list)
            enter=input("What item would you like to add?: ")
            enter=enter.lower()
            if enter=="  ":
                print("I'm sorry you cannot enter a space")
                els=input("Would you like to input something else? ")
                if els=="yes":
                    other=input("What would you like to input? ")
                    list.append(other)
                    print("New list: ",list)
                else:
                    continue
            else:
                list.append(enter)
                print("New list: ", list)
        elif do=="remove":
            print("Current list: ",list)
            item=input("What item would you like to remove?: ")
            if item != list:
                print("That is not on your list.")
                go=input("Would you like to remove something else?: ")
                go=go.lower()
                if go=="yes":
                    new=input("What item would you like to remove?: ")
                    list.remove(new)
                elif go=="no":
                    print("New list: ",list)
        elif do=="relabel":
            finished=input("What item did you finish?: ")
            list.remove(finished)
            done.append(finished)
            print("New list: ",list)
            print("New Finished List: ",done)
        exit=input("Would you like to exit the app?: ")
        exit=exit.lower()
        if exit=="no":
            x=x+1
        elif exit=="yes":
            x=-1
lists()

