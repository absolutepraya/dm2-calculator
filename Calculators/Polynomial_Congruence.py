# Version: 1.01

import sys
from . import Utils

def DESC():
    return """This Polynomial Congruence Calculator will solve the quadratic congruence
of the form ax^2 + bx + c ≡ 0 (mod m) and provide the steps to solve it.
The method used to solve the congruence is by bruteforcing the values
of x from 0 to m-1 and checking if the congruence is satisfied. The steps
will be shown in table format."""

def PROGRAM():
    print("""\033[32m┏┓  ┓         •  ┓  ┏┓                 
┃┃┏┓┃┓┏┏┓┏┓┏┳┓┓┏┓┃  ┃ ┏┓┏┓┏┓┏┓┓┏┏┓┏┓┏┏┓
┣┛┗┛┗┗┫┛┗┗┛┛┗┗┗┗┻┗  ┗┛┗┛┛┗┗┫┛ ┗┻┗ ┛┗┗┗   by absolutepraya
┛                    ┛           
\033[0m
This Polynomial Congruence Calculator will solve the quadratic congruence 
of the form ax^2 + bx + c ≡ 0 (mod m) and provide the steps to solve it. 
The method used to solve the congruence is by bruteforcing the values 
of x from 0 to m-1 and checking if the congruence is satisfied. The steps 
will be shown in table format.

———— I N P U T ————————————————————————————————————————————————————————

Enter the a, b, c, d of polynomial congruence in the form of 
ax^2 + bx + c ≡ 0 (mod m).""")

    # Command line input
    if len(sys.argv) > 1:
        a, b, c, m = map(int, sys.argv[1].split(","))
        print(f"""a = {a}
b = {b}
c = {c}
m = {m}""")
    else:
        # Input inside the program
        a = int(input("a = "))
        b = int(input("b = "))
        c = int(input("c = "))
        m = int(input("m = "))
        print(f"""\033[33m{a}x^2 + {b}x + {c} ≡ 0 (mod {m})\033[0m

———— S T E P S ————————————————————————————————————————————————————————

### SOLVING STEPS

Let's say f(x) = {a}x^2 + {b}x + {c}. We need to find the values of x such 
that f(x) ≡ 0 (mod {m}). We will check the values of x from 0 to {m-1} until
we find 2 values of x that satisfy the congruence.
""")

    # First, find the solutions and all necessary values, and put them in a list
    solutions = []
    calc_str = []
    res_str = []
    solutions_count = 0
    for x in range(m):
        val = a*x**2 + b*x + c
        calc_str.append(f"{a}*{x}^2 + {b}*{x} + {c} = {val}")
        if val % m == 0:
            solutions.append(x)
            solutions_count += 1
            res_str.append(f"{val} ≡ 0 (mod {m})")
            if solutions_count == 2:
                break
        else:
            res_str.append(f"{val} /≡ 0 (mod {m})")

    # Create a header for the table
    header = ['x', 'f(x)', 'Result']
    column_widths = [5, 40, 25]

    # Print the header and the separator
    print('|'.join(f'{title:^{width}}' for title, width in zip(header, column_widths)))
    print('—' * (sum(column_widths) + len(column_widths) - 1))

    # Print the table content
    for row in zip(range(m), calc_str, res_str):
        if "/" in row[2]:
            print('|'.join(f'{str(item):^{width}}' for item, width in zip(row, column_widths)))
        else:
            print('|'.join(f'\033[34m{str(item):^{width}}\033[0m' for item, width in zip(row, column_widths)))

    if solutions_count == 0:
        print("\n\033[33m∴ There are no solutions for the given congruence.\033[0m")
    elif solutions_count == 1:
        print(f"\n\033[33m∴ There is only 1 solution for the given congruence: x = {solutions[0]}\033[0m")
    else:
        print(f"\n\033[33m∴ The solutions for the given congruence are x = {solutions[0]} and x = {solutions[1]}\033[0m")

    exit = Utils.CONFIRM_EXIT()
    if exit:
        return
    else:
        PROGRAM()