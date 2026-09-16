
#Function is add in this calculatot

num1 = float(input("Enter first number: "))
op = (input("Enter operator(+,-,*,/,%,**): "))
num2 = float(input("Enter second number: "))


def addition(a, b):
    return a + b 

def subtract(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return  "Cannot divide by 0"
    
    return a / b

def remainder(a, b):
    return a % b

def power(a, b):
    return a ** b


if op == "+":
    print(addition(num1, num2))
elif op == "-":
    print(subtract(num1, num2))

elif op == "*":
     print(multiplication(num1, num2))

elif op == "/":
    print(division(num1, num2))

elif op == "%":
    print(remainder(num1, num2))

elif op == "**":
    print(power(num1, num2))

else :
    print("invalid input")