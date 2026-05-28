#Sasha Hurd-Groves
#image_generator.py

#Initialize
import webbrowser

#Functions

#Main
url = ["https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/669a6c1e-4a48-4367-803e-f2355c5743ce/dcezz4v-a73ab957-2272-4001-89c5-159c02de4c45.png", #Friends
            "https://cdn.printerval.com/unsafe/960x960/asset/111049560a1d1c1a0d1a1a141d56161d0c571115191f1d564c414d4b484c4b4b4c564b40494f571e14190c544f4d480054484f4d541e5508191c544f4d480049484848541e401e401e40560d4c5612081f", #Full House
            "https://cdn.printerval.com/unsafe/960x960/assets.printerval.com/2023/05/25/646e44b9bc0782.27158673.jpg", #Anne With An E
            "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/i/d96bb958-4e6c-4ce0-9447-fbe226fbbecf/df9ecqe-5c3fda34-f950-4475-a6d1-bcbfa90fc457.jpg"]    #Stranger Things

des= ["An entertaining adult comedy about a group of friends that go through life with romance, drama, and jokes",
      "A family friendly comedy that explores loss, love, and growing up together",
      "A family friendly drama that centers around a strong female lead set in the late 1890s",
      "A drama-led show revolving around the mystical magical world of Hawkins, Indiana"
      ]



def shows():
        print("Welcome To Our Recommended Shows")
        age=input("Do you want family-friendly?")
        if age.lower() == "yes":
            genre=input("Do you want a drama or comedy?")
            if genre.lower() == "drama":
                    webbrowser.open(url[2])
                    print(des[2])
            elif genre.lower() == "comedy":
                    webbrowser.open(url[1])
                    print(des[1])
        elif age.lower() == "no":
            genre=input("Do you want a drama or comedy?")
            if genre.lower() == "drama":
                    webbrowser.open(url[3])
                    print(des[3])
            elif genre.lower() == "comedy":
                    webbrowser.open(url[1])
                    print(des[1])


shows()
