


#Init








import pandas as pd
import time
data=pd.read_csv('CSP Project.csv')
name=data['College'].tolist()
size=data['Size'].tolist()
region=data['Location'].tolist()
state=data['State'].tolist()
major=data['Majors'].tolist()
ad=data['Admittance'].tolist()
grad=data['Graduation Rate'].tolist()
ss=data['Social Scene'].tolist()
in_state=data['In-State '].tolist()
out_state=data['Out-of-State'].tolist()
rank=data['Ranking'].tolist()
















#Function
filter=[]
loc=[]
degree=[]
sizes=[]
def location():                                                     #Finds the location where the school is located
    place=input("Where would you like us to start looking by (State or Region): " )
    if place.upper() =='STATE':
        states=input('Please enter the state: ' )
        states=states.capitalize()
        for i in range(len(data)):
            if states in state[i]:
                loc.append(name[i])
        if (len(loc))==0:
            print("Sorry that is not a valid input, please try again")                                      #If the list contains nothing, the user will get an invalid input
        else:
            print("Your best matched schools for your area are:",loc)
            loc.clear()
    elif place.upper()=='REGION':
        area=input ('Search by (Northeast, East, West, Mid-West): ' )
        area=area.capitalize()
        for i in range(len(data)):
            if area in region[i]:
                loc.append(name[i])
        if (len(loc))==0:
            print('Sorry that is not a valid input, please try again')
        else:
            print("Your best matched schools for your area are:",loc)
            loc.clear()
    elif (len(loc))==0:
            print('Sorry that is not a valid input, please try agian')




def academics():
    study=input('What major would you like to study: ')
    for i in range(len(data)):
        if study in major[i]:                                                                       #Accesses the majors data set to see if what the student input matches selected majors at the universities
            degree.append(name[i])
    if (len(degree))==0:
        time.sleep(1)
        print('Sorry that is not one of the most known majors, please try again')
    else:
        time.sleep(1)
        print("Your best matched schools for your major are:",degree)
    degree.clear()
def price():
    money=input('Is cost of tuition an important factor(Yes,No)?: ')
    school=[]
    if money.upper()=='YES':
        time.sleep(1)
        avg=input ('Enter the max amount you are looking to pay:'  )                    #Finds how much money the student is willing to pay to be stored
        time.sleep(1)
        out=input("First are you looking for in-state,out-of-state tuition cost, or both?: ")
        if out.lower()=="in-state":
            for i in range(len(in_state)):
                if in_state[i]<=avg:                                        #Accesses whether or not what the students put in is lower than the tuition for in-state
                    school.append(name[i])
            time.sleep(1)
            print("Your best matched schools for your maximum price are:",school)
        elif out.lower()=="out-of-state":
            for i in range(len(out_state)):
                if out_state[i]<=avg:
                    school.append(name[i])
            time.sleep(1)
            print("Your best matched schools for your maximum price are:",school)
        elif out.lower()=="both":
            for i in range(len(out_state)):
                if out_state[i] <= avg and in_state[i]<=avg:
                    school.append(name[i])
            time.sleep(1)
            print("Your best matched schools for your maximum price are:",school)
    elif money.upper()=="NO":
        time.sleep(1)
        print("Okay, you may continue on.")
    school.clear()

def sizee():
    sizes.clear()
    scale=input("What size would you be looking for (Medium, or Large)?: ")
    scale=scale.upper()
    if scale.upper()== "MEDIUM":
        for i in range(len(size)):
            if size[i]=="Medium":
                sizes.append(name[i])
        time.sleep(1)
        print("Your best matched schools for your preferred size are:", sizes)
    elif scale== "LARGE":
        for i in range(len(size)):
                if size[i]=="Large":
                    sizes.append(name[i])
        time.sleep(1)
        print("Your best matched schools for your preferred size are:", sizes)
    elif (len(sizes))==0:
        print ("Sorry thats not a valid input")
def admittance():
    filter.clear()
    rate=input("Would you like a guaranteed, match, reach, or far reach school?: ")
    if rate=="guaranteed":
        for i in range(len(ad)):
            if ad[i]>="85":
                filter.append(name[i])
        time.sleep(1)
        print("Your best matches for college are ",filter)




    elif rate=="match":
        for i in range(len(ad)):
            if ad[i]>="50":
                filter.append(name[i])
        time.sleep(1)
        print("Your best matches for college are ",filter)




    elif rate=="reach":
        for i in range(len(ad)):
            if ad[i]>="20":
                filter.append(name[i])
        time.sleep(1)
        print("Your best matches for college are ",filter)




    elif rate=="far reach":
        for i in range(len(ad)):
            if ad[i]<"85":
                filter.append(name[i])
        time.sleep(1)
        print("Your best matches for college are ",filter)
def gradss():
    filter.clear()
    grads=input("Would you like to see a graduation rate for a certain school or see the schools with a certain graduation rate(1 or 2)?: ")
    if grads=="1":
        school=input("What college would you like to see the graduation rate of?")
        for i in range(len(name)):
            if school in name[i]:
                filter.append(grad[i])
                print(filter)
        if (len(filter))== 0:
                print("Sorry that is not a valid input, please try a different name")

    elif grads=="2":
        rate=input("What is the lowest graduation rate that you are okay with?: ")
        for i in range(len(grad)):
            if rate <= grad[i]:
                filter.append(name[i])
                print(filter)
def social():
    filter.clear()
    socials=input("Is the social scene important you?: ")
    socials=socials.upper()
    if socials== "NO":
        time.sleep(1)
        print("If the social scene is not important you may continue.")
    elif socials== "YES":
        soc=input("What kind of social scene are you okay with (Low, Moderate, Good, Amazing, or Great)?: ")
        soc=soc.capitalize()
        for i in range(len(ss)):
            if soc in ss[i]:
                filter.append(name[i])
        time.sleep(1)
        print("The schools that match your social scene are ", filter)
def ranking():
    value=[]
    bad=[]
    ranks=input("Do you want to filter schools by their ranking or search the the rank of a specific school (Filter, Search )?: " )
    ranks=ranks.upper()
    if ranks == "SEARCH":
        scho=input("What school would you like the rank of?: ")
        scho=scho.capitalize()
        for i in range(len(name)):
            if scho in name[i]:
                value.append(rank[i])
        time.sleep(1)
        print("Your school is ranked at", value)
        if len(value) == 0:
            print("I am sorry that is not a school that we have in our recevoir, please input a different name.")
    elif ranks == "FILTER":
        mins=input("What it the lowest rank you are ok with?: ")
        mins=int(mins)
        for i in range(len(rank)):
            if mins <= rank[i]:
                value.append(name[i])
            else:
                bad.append(name[i])
        time.sleep(1)
        print("Here are schools at or above your desired rank", value)
def info(university):
    filter.clear()
    for i in range(len(data)):
        if university in name[i]:
            filter.append(data.loc[i])
            print(filter)
    if (len(filter))==0:
        print('Sorry that is not a valid input, please try a different name')
def menu():
    x=0
    print("Welcome to College Search! We are here to help you find your perfect University and get some useful info!")
    print("                       ")
    print("====== Main Menu ======")
    print("                       ")
    while x==0:
        choose= input("Do you want help finding a college or info on a particular college(info,help): ")
        time.sleep(1)
        if choose=="info":
            print("                       ")
            university=input("Enter the name of the school you want more information on: " )
            info(university)
            x=x+1
        elif choose=="help":
            sort=input("Would you like to search colleges by \nRank(a) \nSize(b) \nLocation(c) \nCost(d) \nGraduation rates(e) \nAdmittance rates(f) \nMajor(g) \nSchool Culture(h) \n: ")
            sort=sort.upper()
            if sort =="A":
                ranking()
                x=x+1
            elif sort== "B":
                sizee()
                x=x+1
            elif sort== "C":
                location()
                x=x+1
            elif sort== "D":
                price()
                x=x+1
            elif sort=="E":
                gradss()
                x=x+1
            elif sort== "F":
                admittance()
                x=x+1
            elif sort=="G":
                academics()
                x=x+1
            elif sort=="H":
                social()
                x=x+1
            else:
                print("Sorry thats not one of our search categories")
                x=x+1
        else:
            print("               ")
            print("Incorrect format please try again.")
            print("               ")

        while x==1:
            print("Would you like to find a college, info, or to quit?")
            choose=input("C = college       I = info         Q = Quit\n :")
            time.sleep(1)
            choose=choose.upper()
            if choose == "C":
                sort=input("Would you like to search colleges by \nRank(a) \nSize(b) \nLocation(c) \nCost(d) \nGraduation rates(e) \nAdmittance rates(f) \nMajor(g) \nSchool Culture(h) \n: ")
                sort=sort.upper()
                if sort =="A":
                    ranking()


                elif sort== "B":
                    sizee()


                elif sort== "C":
                    location()


                elif sort== "D":
                    price()


                elif sort=="E":
                    gradss()


                elif sort== "F":
                    admittance()


                elif sort=="G":
                    academics()


                elif sort=="H":
                    social()


                else:
                    print("Sorry thats not one of our search categories")
            elif choose == "I":
                university=input("Enter the name of the school you want more information on:" )
                info(university)
            elif choose == "Q":
                break






#Main
menu()








#Best Colleges
#Website Name: RippleMatch
#Author Name: RippleMatch
#Website URL: https://ripplematch.com/insights/the-best-public-university-in-every-state-d0379bd3
#What Regions Each State Is In
#Website Name: Wikipedia
#Author Name: Unknown
#Website URL: https://en.wikipedia.org/wiki/List_of_regions_of_the_United_States


