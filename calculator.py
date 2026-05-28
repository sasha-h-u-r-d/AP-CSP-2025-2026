#calculator.py
#SashaHurd
#Create a Python program that asks the user to enter two numbers and an operation, then prints the result of that operation.

def main():
    print("Welcome To  The Python Calculator")
    num1=int(input("Please put in your first number"))
    num2=int(input("Please put in your second number"))
    operator=input("Please put in your operative symbol:")
    if operator == "+":
        print(calc_sum(num1,num2))
    if operator == "-":
        print(calc_sub(num1,num2))
    if operator == "*":
        print(calc_mult(num1,num2))
    if operator == "/":
        print(calc_div(num1,num2))

def calc_sum(x, y):
    return x + y
def calc_sub(x, y):
    return x - y
def calc_mult(x, y):
    return x * y
def calc_div(x, y):
    return x / y
main()
