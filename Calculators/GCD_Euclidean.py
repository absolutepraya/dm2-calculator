from . import Utils


def DESC():
    return """Shows the steps of the Euclidean algorithm to find the GCD
of two numbers."""


@Utils.HANDLE_CALC_ERRORS
def PROGRAM(invalid=False):
    print(
        """\033[32m┏┓   ┓• ┓        ┏┓┏┓┳┓
┣ ┓┏┏┃┓┏┫┏┓┏┓┏┓  ┃┓┃ ┃┃
┗┛┗┻┗┗┗┗┻┗ ┗┻┛┗  ┗┛┗┛┻┛  by absolutepraya\033[0m

Shows the steps of the Euclidean algorithm to find the GCD 
of two numbers.

———— I N P U T ————————————————————————————————————————————————————————

Enter two numbers for GCD(x, y). (CTRL+C to quit)"""
        + (
            "\n\n\033[31mInvalid input. Please enter integers only.\033[0m\n"
            if invalid
            else ""
        )
    )

    num1 = input("x = ")
    num2 = input("y = ")

    # Check if the input is an integer
    if not Utils.CHECK_INT_INPUT(num1, num2):
        Utils.CLEAR_TERMINAL()
        PROGRAM(invalid=True)
        return
    else:
        num1 = int(num1)
        num2 = int(num2)

    print(
        f"""\033[33mGCD({num1}, {num2})\033[0m

———— S T E P S ————————————————————————————————————————————————————————

### SOLVING STEPS
"""
    )

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
