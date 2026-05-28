#Parity.py
#Sasha Hurd-Groves
#This function should take one parameter, a number x. It should check whether the number is even or odd using the remainder operator %. The function should return True if the number is even, and False if it is odd.


def main():
    num=int(input("Please enter a number: "))
    if is_even(num):
        print("EVEN")
    else:
        print("ODD")
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False

main()
