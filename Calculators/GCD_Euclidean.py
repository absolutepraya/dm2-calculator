# Version: 1.20

import sys
from . import Utils

def DESC():
    return """Shows the steps of the Euclidean algorithm to find the GCD
of two numbers."""

def PROGRAM():
    print("""\033[32m┏┓   ┓• ┓        ┏┓┏┓┳┓
┣ ┓┏┏┃┓┏┫┏┓┏┓┏┓  ┃┓┃ ┃┃
┗┛┗┻┗┗┗┗┻┗ ┗┻┛┗  ┗┛┗┛┻┛  by absolutepraya\033[0m

Shows the steps of the Euclidean algorithm to find the GCD 
of two numbers.

———— I N P U T ————————————————————————————————————————————————————————

Enter two numbers for GCD(x, y).""")

    # Command line arguments
    if len(sys.argv) > 1:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    # Input inside the program
    else:
        num1 = int(input("x = "))
        num2 = int(input("y = "))
    print(f"""\033[33mGCD({num1}, {num2})\033[0m

———— S T E P S ————————————————————————————————————————————————————————

### SOLVING STEPS
""")

    # Euclidean algorithm
    x = num1
    y = num2
    while y != 0:
        print(f"{x} = {y} * {x // y} + {x % y}")
        x, y = y, x % y

    print(f"\n\033[33m∴ Therefore, GCD({num1}, {num2}) = {x}\033[0m")

    exit = Utils.CONFIRM_EXIT()
    if exit:
        return
    else:
        PROGRAM()