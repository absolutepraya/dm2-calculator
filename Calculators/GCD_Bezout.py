from . import Utils


def DESC():
    return """Shows the steps of the Bezout's theorem to express GCD as
linear number combination (GCD(x, y) = m * x + n * y)."""


@Utils.HANDLE_CALC_ERRORS
def PROGRAM(invalid=False):
    print(
        """\033[32m┳┓          ┏┓┏┓┳┓
┣┫┏┓┓┏┓┓┏╋  ┃┓┃ ┃┃
┻┛┗ ┗┗┛┗┻┗  ┗┛┗┛┻┛  by absolutepraya\033[0m

Shows the steps of the Bezout's theorem to express GCD as 
linear number combination (GCD(x, y) = m * x + n * y).

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

(1) To find m and n, use the Euclidean algorithm to find the
GCD of x and y.
"""
    )

    # Euclidean algorithm
    x = num1
    y = num2
    while y != 0:
        print(f"{x} = {y} * {x // y} + {x % y}")
        x, y = y, x % y
    print(f"GCD({num1}, {num2}) = {x}")

    print(
        """
(2) Then, work backwards to express the GCD as a linear
combination of x and y. The steps are shown below.
"""
    )

    # Bezout's theorem
    x = num1
    y = num2
    m = 1
    n = 0
    m_prev = 0
    n_prev = 1
    while y != 0:
        q = x // y
        x, y = y, x % y
        m, m_prev = m_prev, m - q * m_prev
        n, n_prev = n_prev, n - q * n_prev
        print(f"{x} = ({m}) * {num1} + ({n}) * {num2}")

    print(
        f"""
m = {m}
n = {n}
\033[33m∴ Therefore, GCD({num1}, {num2}) = {m} * {num1} + {n} * {num2}\033[0m"""
    )

    exit = Utils.CONFIRM_EXIT()
    if exit:
        return
    else:
        PROGRAM()
