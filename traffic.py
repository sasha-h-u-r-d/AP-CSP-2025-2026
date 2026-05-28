#Traffic.py
#Sasha Hurd-Groves

# Chicago Streets
chicago_streets = [
    "State St", "Michigan Ave", "Wacker Dr", "Lake Shore Dr", "Western Ave",
    "Halsted St", "Milwaukee Ave", "Fullerton Ave", "Grand Ave", "Belmont Ave",
    "Irving Park Rd", "North Ave", "Lawrence Ave", "Foster Ave", "Bryn Mawr Ave",
    "Peterson Ave", "Touhy Ave", "Devon Ave", "Addison St", "Montrose Ave",
    "Damen Ave", "Elston Ave", "Lincoln Ave", "Archer Ave", "Pulaski Rd",
    "Cicero Ave", "Kedzie Ave", "California Ave", "Homan Ave", "Central Park Ave",
    "Narragansett Ave", "Austin Blvd", "Ashland Ave", "Central Ave", "Laramie Ave",
    "Kostner Ave", "Crawford Ave", "Columbus Dr", "LaSalle St", "Dearborn St",
    "Clark St", "Broadway", "Sheridan Rd", "Ridge Ave", "Clybourn Ave",
    "Ogden Ave", "Roosevelt Rd", "Cermak Rd", "Pershing Rd", "Garfield Blvd"
]

# Traffic Volume (cars recorded per hour)
traffic_volume = [
    2800, 5200, 2900, 2500, 4100,
    2100, 2400, 4800, 1800, 2300,
    2200, 4300, 1900, 1500, 1400,
    2600, 2100, 1700, 2400, 1800,
    2000, 1900, 3900, 2500, 2800,
    2900, 2200, 1600, 1200, 1100,
    1300, 1700, 4500, 2100, 1800,
    1400, 1300, 2900, 2700, 2400,
    2200, 2500, 2600, 2100, 1900,
    2300, 2800, 2400, 2100, 1500
]
def traffic(item_name):
    i=0
    streets=[]
    for i in range(len(items)):
        if item_name==items[i]:
            print(prices[i])
            return prices[i]
        else:
            i=i+1
def traffic(volume):
    i=0
    traffic=[]
    for i in range(len(chicago_streets)):
        if traffic_volume[i]>=(volume):
            traffic.append(chicago_streets[i])
            i=i+1
        else:
            i=i+1
    print(traffic)
traffic_volume.sort()
print(chicago_streets[49])
traffic(3000)
