#NestedIf
#Sasha
#Make A Name Generator


def character():
        print("Welcome To Which Harry Potter Character Are You?")
        gender=input("Are you a Boy or Girl?:")
        if gender.lower() == "boy":
            good=input("Is your house Popular or Not Really?:")
            if good.lower() == "popular":
                house=input("Are you in Gryffindor or Slytherin?:")
                if house.lower() == "gryffindor":
                    print("Congrats you are Harry Potter")
                elif house.lower() == "slytherin":
                    print("Congrats you are Draco Malfoy")
                else:
                    print("PUT IN THE RIGHT INPUT")
            elif good.lower() == "not really":
                house=input("Are you in Hufflepuff or Ravenclaw?:")
                if house.lower() == "hufflepuff":
                    print("Congrats you are Cedric Diggory")
                elif house.lower() == "ravenclaw":
                    print("Congrats you are Roger Davies")
                else:
                    print("PUT IN THE RIGHT INPUT")
        if gender.lower() == "girl":
            good=input("Is your house Popular or Not Really?:")
            if good.lower() == "popular":
                house=input("Are you in Gryffindor or Slytherin?:")
                if house.lower() == "gryffindor":
                    print("Congrats you are Hermione Granger")
                elif house.lower() == "slytherin":
                    print("Congrats you are Andromeda Tonks")
                else:
                    print("PUT IN THE RIGHT INPUT")
            elif good.lower() == "not really":
                house=input("Are you in Hufflepuff or Ravenclaw?:")
                if house.lower() == "hufflepuff":
                    print("Congrats you are Helga Hufflepuff")
                elif house.lower() == "ravenclaw":
                    print("Congrats you are Luna Lovegood")
                else:
                    print("PUT IN THE RIGHT INPUT")


character()

