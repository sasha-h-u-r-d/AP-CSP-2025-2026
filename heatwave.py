#Heatwave.py
#Sasha Hurd-Groves
# The dates as strings
july_days = [ "July 1", "July 2", "July 3", "July 4", "July 5", "July 6", "July 7", "July 8", "July 9", "July 10", "July 11", "July 12", "July 13", "July 14", "July 15", "July 16", "July 17", "July 18", "July 19", "July 20", "July 21", "July 22", "July 23", "July 24", "July 25", "July 26", "July 27", "July 28", "July 29", "July 30", "July 31" ]

# The temperatures in Fahrenheit
july_temps_f = [
    82, 84, 87, 89, 93, 95, 91, 88, 86, 84,
    86, 89, 95, 97, 98, 101, 97, 93, 89, 87,
    86, 91, 95, 93, 89, 87, 84, 86, 89, 93, 91
]

def heatwave(temps):
    i=0
    days=[]
    for i in range(len(july_temps_f)):
        if july_temps_f[i]>=(temps):
            days.append(july_days[i])
            i=i+1
        else:
            i=i+1
    print(days)
heatwave(92)
