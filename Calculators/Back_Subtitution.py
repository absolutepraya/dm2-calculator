from . import Utils


def DESC():
    return """Back Sub calculator solves linear congruences usign back substitution 
method, so it does not need for the modulo condition to be a prime 
relative pair. The supported congruence form is x ≡ a (mod m)."""


@Utils.HANDLE_CALC_ERRORS
def PROGRAM(invalid=False):
    print(
        """\033[32m┳┓   ┓   ┏┓  ┓  •    •    
┣┫┏┓┏┃┏  ┗┓┓┏┣┓╋┓╋┓┏╋┓┏┓┏┓
┻┛┗┻┗┛┗  ┗┛┗┻┗┛┗┗┗┗┻┗┗┗┛┛┗ by absolutepraya\033[0m

Back Sub calculator solves linear congruences usign back substitution 
method, so it does not need for the modulo condition to be a prime 
relative pair. The supported congruence form is x ≡ a (mod m).

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
        a, m = map(str, input(f"a{i+1}, m{i+1} = ").replace(" ", "").split(","))
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

    alphabet = "tuvwxyzfghijkl"

    print(
        f"""\n\033[0m——— S T E P S ————————————————————————————————————————————————————————

### SOLVING STEPS

(1) Change the form of the first congruence from x ≡ a (mod m) to x = a + mt.
"""
    )

    # Change the form of the first congruence
    a, m = congruences[0]
    print(
        f"""x ≡ {a} (mod {m})
x = {a} + {m}t
"""
    )

    counter = 1
    counter2 = 0
    k = 0

    for i in range(2, len(congruences) + 2, 2):
        a2, m2 = congruences[i - counter]

        print(
            f"""({i}) Substitute the x into the next congruence, then change the 
form into {alphabet[counter2]} = a + m{alphabet[i-counter]}.
"""
        )

        # Substitute the x into the next congruence
        print(
            f"""x ≡ {a2} (mod {m2})
{a} + {m}{alphabet[i-counter-1]} ≡ {a2} (mod {m2})
{m}{alphabet[i-counter-1]} ≡ {a2 - a} (mod {m2})"""
        )

        # If the a is not divisible by m
        if (a2 - a) % m != 0:
            # Find the congruence of (a2 - a) mod m2 that can be divided by m
            for j in range(int(a2 - a), int(-100000 * m2), -1):
                if j % m2 == (a2 - a) % m2 and j % m == 0:
                    print(f"{m}{alphabet[i-counter-1]} ≡ {j} (mod {m2})")
                    k = j
                    break
        else:
            k = a2 - a
            print(f"{m}{alphabet[i-counter-1]} ≡ {k} (mod {m2})")

        print(f"{alphabet[i-counter-1]} ≡ {int(k/m)} (mod {m2})")

        l = 0

        # If the a is negative, find the smallest positive integer congruence
        if (k) / m < 0:
            for j in range(1, 2 * m2):
                if (j - ((k) / m) % m2) % m2 == 0:
                    print(f"{alphabet[i-counter-1]} ≡ {j} (mod {m2})")
                    l = j
                    break
        else:
            l = int(k / m)

        print(f"\n{alphabet[i-counter-1]} = {l} + {m2}{alphabet[i-counter]}\n")

        # t, u, v, or etc value
        a3, m3 = l, m2

        print(
            f"""({i+1}) Substitute {alphabet[i-counter-1]} back into the initial x equation.

x = {a} + {m}{alphabet[i-counter-1]}
x = {a} + {m}({l} + {m2}{alphabet[i-counter]})
x = {a} + {m*l} + {m*m2}{alphabet[i-counter]}
x = {a + m*l} + {m*m2}{alphabet[i-counter]}
"""
        )

        a, m = m * a3 + a, m * m3

        counter += 1
        counter2 += 1

    print(
        f"""({i+2}) Change the x to modulo form.
x ≡ {a} (mod {m})

\033[33m∴ Therefore, the solution is x ≡ {a} (mod {m}).\033[0m"""
    )

    exit = Utils.CONFIRM_EXIT()
    if exit:
        return
    else:
        PROGRAM()
