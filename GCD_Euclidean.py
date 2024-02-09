# Version: 1.0

import sys

print("""┏┓   ┓• ┓        ┏┓┏┓┳┓
┣ ┓┏┏┃┓┏┫┏┓┏┓┏┓  ┃┓┃ ┃┃
┗┛┗┻┗┗┗┗┻┗ ┗┻┛┗  ┗┛┗┛┻┛  by absolutepraya

Shows the steps of the Euclidean algorithm to find the GCD 
of two numbers.

————————————————————————————————————————————————————————————
""")

# Command line arguments
if len(sys.argv) > 1:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
# Input inside the program
else:
    print("Enter two numbers for GCD(x, y).")
    num1 = int(input("x = "))
    num2 = int(input("y = "))
print(f"""GCD({num1}, {num2})

————————————————————————————————————————————————————————————

### SOLVING STEPS

""")

# Euclidean algorithm
x = num1
y = num2
while y != 0:
    print(f"{x} = {y} * {x // y} + {x % y}")
    x, y = y, x % y

print(f"\n∴ Therefore, GCD({num1}, {num2}) = {x}")