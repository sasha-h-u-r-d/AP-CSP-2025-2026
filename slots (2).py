#Sasha Hurd and Isla Hudecek

#Imports
import random
import time


#Function


def slots():
	slots=['★','☆', '✪','7']
	print("Slot machine symbols are ", slots)
	deposit=int(input("Would you like to buy 50, 100, or 500 credits? "))
	credits=0
	if deposit==50:
		credits=credits+50
	elif deposit==100:
		credits=credits+100
	elif deposit==500:
		credits=credits+500
	print(f"You have {credits} credits")
	print("Each spin costs 10 credits")
	choice=input("Press 'S' to spin or 'Q' to quit: ")
	while choice=="S" and credits>10:
		slots=[['☆','☆','☆','☆','☆','☆','☆','☆','☆','★','★','★','★','★','★','★','✪','✪','✪','7']]
		credits=credits-10
		x=random.choice(slots)
		y=random.choice(slots)
		z=random.choice(slots)
		print("Spinning............")
		time.sleep(1)
		print(x,y,z)
		if x=="7" and y=="7" and z== "7":
			print ("Jack Pot")
			credits=credits+500
			print("Credits= ", credits)
		elif x=="☆" and y=="☆" and z=="☆":
			print("You Win")
			credits=credits+50
			print("Credits= ", credits)
		elif x=="★" and y=="★" and z=="★":
			print ('You Win')
			credits=credits+100
			print("Credits= ", credits)
		elif x=="✪" and y=="✪" and z=="✪":
			print("You Win")
			credits=credits+150
			print("Credits= ", credits)
		else:
			print("You lose")
			print("Credits= ", credits)
		choice=input("Press 'S' to spin or 'Q' to cash out: ")
		choice.upper()
		if credits<11:
			print("I'm sorry you do not have enough credits to play")
			print("Please enter more credits")
			deposit=int(input("Would you like to buy 50, 100, or 500 credits? "))
			if deposit==50:
				credits=credits+50
			elif deposit==100:
				credits=credits+100
			elif deposit==500:
				credits=credits+500
			print(f"You have {credits} credits")
		if choice=="Q":
			print("Credits: ",credits)
			break

def slot():
	credits=10000
	house=0
	for i in range(1000):
		slots=['☆','☆','☆','☆','☆','☆','☆','☆','☆','★','★','★','★','★','★','★','✪','✪','✪','7']
		credits=credits-10
		house=house+10
		x=random.choice(slots)
		y=random.choice(slots)
		z=random.choice(slots)
		print(x,y,z)
		if x=="7" and y=="7" and z== "7":
			print ("Jack Pot")
			credits=credits+500
			house=house-500
			print("Credits= ", credits)
		elif x=="☆" and y=="☆" and z=="☆":
			print("You Win")
			credits=credits+50
			house=house-50
			print("Credits= ", credits)
		elif x=="★" and y=="★" and z=="★":
			print ('You Win')
			credits=credits+100
			house=house-100
			print("Credits= ", credits)
		elif x=="✪" and y=="✪" and z=="✪":
			print("You Win")
			credits=credits+150
			house=house-150
			print("Credits= ", credits)
		else:
			print("You lose")
		print("Casino= ", house)


#Main
slot()
