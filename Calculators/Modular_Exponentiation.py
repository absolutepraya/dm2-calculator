# Version: 1.26

import sys
from . import Utils

def DESC():
    return """This Modular Exponentiation calculator does not just 
return the result, but also shows the steps of the calculation using
Modular Exponentiation algorithm. The steps are shown in a table format."""

def PROGRAM():
    print("""\033[32m┳┳┓   ┓  ┓      ┏┓             •   •    
┃┃┃┏┓┏┫┓┏┃┏┓┏┓  ┣ ┓┏┏┓┏┓┏┓┏┓┏┓╋┓┏┓╋┓┏┓┏┓
┛ ┗┗┛┗┻┗┻┗┗┻┛   ┗┛┛┗┣┛┗┛┛┗┗ ┛┗┗┗┗┻┗┗┗┛┛┗  by absolutepraya
                    ┛
\033[0m
This Modular Exponentiation calculator does not just 
return the result, but also shows the steps of the calculation using
Modular Exponentiation algorithm. The steps are shown in a table format.

———— I N P U T ————————————————————————————————————————————————————————

Enter the base, exponent, and mod of the equation.""")

    # Command line input
    if len(sys.argv) > 1:
        base = int(sys.argv[1])
        exponent = int(sys.argv[2])
        mod = int(sys.argv[3])
        print(f"""Base     =  {base}
Exponent =  {exponent}
Mod      =  {mod}""")
    # Input inside the program
    else:
        base = int(input("Base     =  "))
        exponent = int(input("Exponent =  "))
        mod = int(input("Mod      =  "))
    print(f"""\033[33m{base}^{exponent} % {mod}\033[0m

———— S T E P S ————————————————————————————————————————————————————————
""")

    # Power calculator
    exp_bin = bin(exponent)[2:]
    exp_bin_len = len(exp_bin)
    pow_lst = [base % mod]
    pow_str = []
    for i in range(exp_bin_len - 1):
        pow_lst.append(pow_lst[i] ** 2 % mod)
        pow_str.append(f"{pow_lst[i]}^2 % {mod} = {pow_lst[i]**2} % {mod} = {pow_lst[i + 1]}")

    # Result calculator
    exp_bin_rev = exp_bin[::-1]
    res_lst = []
    res_str = []
    for i in range(exp_bin_len):
        if exp_bin_rev[i] == "1":
            if len(res_lst) == 0:
                res_lst.append((1 * pow_lst[i]) % mod)
                res_str.append(f"1 * {pow_lst[i]} % {mod} = {res_lst[i]}")
            else:
                res_lst.append((res_lst[-1] * pow_lst[i]) % mod)
                res_str.append(f"{res_lst[-2]} * {pow_lst[i]} % {mod} = {res_lst[i]}")
        else:
            if len(res_lst) == 0:
                res_lst.append(1)
            else:
                res_lst.append(res_lst[-1])
            res_str.append(f"{res_lst[i]}")

    # Tidying up the lists for the table
    pow_lst = pow_lst[1:]
    pow_lst.append("-")
    pow_str.append("-")

    # Print initialization
    print(f"""### INITIALIZATION

Exponent in binary :  {exp_bin}
Initial result     :  1
Initial power      :  {base} % {mod} = {base % mod}

### CALCULATION
""")

    # Create a header for the table
    header = ['Bit', 'Result', 'Calculate Power', 'Power']
    column_widths = [5, 25, 40, 7]

    # Print the header and the separator
    print('|'.join(f'{title:^{width}}' for title, width in zip(header, column_widths)))
    print('—' * (sum(column_widths) + len(column_widths) - 1))

    # Iterate over the lists simultaneously and print rows
    for row in zip(list(exp_bin_rev), res_str, pow_str, pow_lst):
        print('|'.join(f'{str(item):^{width}}' for item, width in zip(row, column_widths)))

    print(f"\n\033[33m∴ Therefore, the result is {res_lst[i]}\033[0m")

    exit = Utils.CONFIRM_EXIT()
    if exit:
        return
    else:
        PROGRAM()