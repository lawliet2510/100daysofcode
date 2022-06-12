from time import sleep
import os
def add(a, b):
    return a + b

def substract(a, b):
    return a - b

def mutilply(a, b):
    return a * b

def devide(a, b):
    return a / b

operators = {
    "+": add,
    "-": substract,
    "*": mutilply,
    "/": devide
}

def calc():
    a = float(input("What's the first number: "))
    for op in operators:
        print(op)
    should_continue = True
    while should_continue:
        operator_symbol = input("Pick a operator: ")
        b = float(input("What's the next number: "))
        answer = operators[operator_symbol](a, b)
        print(f"{a} {operator_symbol} {b} = {answer}")
        if(input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y"):
            a = answer
        else:
            should_continue = False
            sleep(0)
            os.system('cls')
            calc()

calc()

        