#calculator.py
#by Ashley Cook

#calculator functions
#add
from art import calc_logo
def add(n1, n2):
    return n1 + n2
#subtract
def subtract(n1, n2):
    return n1 - n2
#multiply
def multiply(n1, n2):
    return n1 * n2
#divide
def divide(n1,n2):
    return n1 / n2

#dictionary of functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}
def calculator():
    print(calc_logo)
    num1 = float(input("What is the first number:\n"))
    for key in operations:
        print(key)
    should_continue = True

    while should_continue:
        operation_symbol = input("Please pick an operation from above:\n")
        num2 = float(input("What is the next number?\n"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation\n") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()