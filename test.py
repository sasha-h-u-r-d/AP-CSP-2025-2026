#Function
scores = [88, 42, 95, 70, 63, 82, 55, 91, 74, 85,38, 77, 90, 61, 89, 72, 59, 98, 45, 81,67, 73, 88, 52, 94, 79, 100, 68, 83, 71]
print(min(scores))
print(max(scores))
print(sum(scores)/len(scores))
scores.sort()
print(scores[0:3])
def add():
    x=0
    for i in range(len(scores)):
        scores[x]=scores[x]+5
        x=x+1
    print(scores)
#Main
add()
