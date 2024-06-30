import math
from . import Utils


def DESC():
    return """Chinese Remainder Theorem (CRT) calculator that can solve the system of linear
congruences with the steps. The supported congruence form is x ≡ a (mod m)."""


@Utils.HANDLE_CALC_ERRORS
def PROGRAM(invalid=False):
    print(
        """\033[32m┏┓┓ •         ┳┓       •   ┓      ┏┳┓┓            
┃ ┣┓┓┏┓┏┓┏┏┓  ┣┫┏┓┏┳┓┏┓┓┏┓┏┫┏┓┏┓   ┃ ┣┓┏┓┏┓┏┓┏┓┏┳┓
┗┛┛┗┗┛┗┗ ┛┗   ┛┗┗ ┛┗┗┗┻┗┛┗┗┻┗ ┛    ┻ ┛┗┗ ┗┛┛ ┗ ┛┗┗  by absolutepraya\033[0m
    
Chinese Remainder Theorem (CRT) calculator that can solve the system of linear
congruences with the steps. The supported congruence form is x ≡ a (mod m).
    
——— I N P U T ————————————————————————————————————————————————————————
    
How many congruences do you want to solve? (CTRL+C to quit)"""
        + (
            "\n\n\033[31mInvalid input. Please enter integers only.\033[0m\n"
            if invalid
            else ""
        )
    )

    n = input("Number of congruences = ")

    # Check if the input is an integer
    if not Utils.CHECK_INT_INPUT(str(n)):
        Utils.CLEAR_TERMINAL()
        PROGRAM(invalid=True)
        return
    else:
        n = int(n)

    print("\nInput a and m for each congruence x ≡ a (mod m). Divide them with comma.")
    congruences = []
    for i in range(n):
        a, m = map(str, input(f"a{i+1}, m{i+1} = ").split(","))
        congruences.append((a, m))
    
    # Check if all inputs are integers
    if not Utils.CHECK_INT_INPUT(*[item for a, m in congruences for item in (a, m)]):
        Utils.CLEAR_TERMINAL()
        PROGRAM(invalid=True)
        return
    else:
        congruences = [(int(a), int(m)) for a, m in congruences]

    print(f"""\n\033[33mSystem of linear congruences:""")
    for i, (a, m) in enumerate(congruences):
        print(f"x ≡ {a} (mod {m})")

    print(
        f"""\n\033[0m——— S T E P S ————————————————————————————————————————————————————————

### SOLVING STEPS

(1) Find the product of all modulus, M = m1 * m2 * ... * mk.
"""
    )

    # Find the product of all modulus
    M = 1
    for m in [t[1] for t in congruences]:
        M *= m

    multiplication_string = " * ".join([str(t[1]) for t in congruences])
    print(f"M = {multiplication_string} = {M}")

    print("\n(2) Find Mk where Mk = M / mk for each congruence.\n")

    # Find Mk for each congruence
    Mks = []
    temp_k = 0
    for a, m in congruences:
        Mk = M // m
        Mks.append(Mk)
        temp_k += 1
        print(f"M{temp_k} = {M} / {m} = {Mk}")

    print("\n(3) Find Yk which is the inverse modulo of Mk modulo mk.\n")

    # Find Yk for each congruence
    Yks = []
    temp_k = 0
    for a, m in congruences:
        Mk = Mks[temp_k]
        temp_k += 1
        if math.gcd(Mk, m) == 1:
            Yk = pow(Mk, -1, m)
            Yks.append(Yk)
            print(f"Y{temp_k} = inverse of {Mk} modulo {m} = {Yk}")
        else:
            print(
                f"""Mk = {Mk} is not invertible modulo {m}

If Mk is not invertible modulo mk, then the system of linear congruences
does not have a solution.

\033[33m∴ The system of linear congruences can not be solved with CRT.\033[0m

* Note: You might have to do adjustments to the congruences to make them solvable.
        (e.g. when the remainders are the same, you can try merging them using 
        LCM of the modulus)"""
            )
            exit()

    print("\n(4) Find the solution (x) by summing up the product of a, Mk, and Yk.\n")

    # Find the solution
    x = 0
    for i, (a, m) in enumerate(congruences):
        Mk = Mks[i]
        Yk = Yks[i]
        x += a * Mk * Yk
        x_str = f"a{i+1} * M{i+1} * Y{i+1} = {a} * {Mk} * {Yk} = {a * Mk * Yk}"
        print(x_str)
    print("—" * (len(x_str) + 2) + " +" + "\n" + "Total (x) = " + str(x))

    print("\n(5) Find the smallest non-negative solution by taking x modulo M.\n")

    # Find the smallest non-negative solution
    x_new = x % M
    print(
        f"""x ≡ x mod M
x ≡ {x} (mod {M})
x ≡ {x_new} (mod {M})"""
    )

    print(
        f"""\n\033[33m∴ Therefore, the solutions are all x where x ≡ {x_new} (mod {M})
↪ x = [..., {x_new-2*M}, {x_new-M}, {x_new}, {x_new+M}, {x_new+2*M}, ...]\033[0m"""
    )

    exit = Utils.CONFIRM_EXIT()
    if exit:
        return
    else:
        PROGRAM()
