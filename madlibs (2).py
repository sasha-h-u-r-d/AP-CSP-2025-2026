#Madlibs.py
#To create a fun and interactive game that allows users to input words and generate a nonsensical story.

#Init
import random
#Functions
#Gather Input

#Story
def madlibs():
    choice=input("Would you like to randomize your choice for the day, building, adjective, and action?: ")
    if choice == "yes":
        building=("Burj Khalifa", "Siers Tower", "Eiffel Tower", "Statue of Liberty")
        day=("Monday", "Tuesday", "Wednesday", "Saturday")
        adjectives=("wild", "loose", "lowkenuinely", "prolly not")
        action=("yeeted", "purged", "wrestled", "lenovoed")
        tall_building=random.choice(building)
        selected_day=random.choice(day)
        adjective=random.choice(adjectives)
        tense=random.choice(action)
        random_number=input("A Number: ")
        month=input("A Month: ")
        famous=input("Famous Person: ")
        cute=input("A Cute Animal: ")
        sad=input("A Sad Historic Event: ")
    if choice == "no":
        selected_day=input("Day Of The Week: ")
        random_number=input("A Number: ")
        month=input("A Month: ")
        famous=input("Famous Person: ")
        tall_building=input("A Really Tall Building: ")
        sad=input("A Sad Historic Event: ")
        adjective=input("An Adjective: ")
        cute=input("A Cute Animal: ")
        tense=input("A Past Tense Verb: ")

    print(f"""On \033[1m{selected_day.upper()}\033[0m the \033[1m{random_number.upper()}\033[0m of \033[1m{month.upper()}\033[0m, me and \033[1m{famous.upper()}\033[0m went to the top of \033[1m{tall_building.upper()}\033[0m. Turns out it was a bad day to do that, because it just happened to be \033[1m{sad.upper()}\033[0m. We almost got trapped but thankfully, a \033[1m{adjective.upper()}\033[0m group of \033[1m{cute.upper()}\033[0m saved me and \033[1m{tense.upper()}\033[0m me away""")

madlibs()
