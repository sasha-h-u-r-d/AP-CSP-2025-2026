#playback.py
#SashaHurd
#Implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods)

def sentence():
    sentence=input("Please type out a sentence")
    print(sentence.replace(" ", "..."))
sentence()
