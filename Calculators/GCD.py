import math
from functools import reduce
from . import Utils


def DESC():
    return """GCD calculator that can take unlimited amount of numbers,
and shows the steps (For example, you can do GCD(x, y, z, ...)). 
The method used is by finding the prime roots of the number, and find the 
maximum amount of each square root among the numbers."""


@Utils.HANDLE_CALC_ERRORS
def PROGRAM(invalid=False):
    print(
        """\033[32m┏┓┏┓┳┓
┃┓┃ ┃┃
┗┛┗┛┻┛  by absolutepraya\033[0m

GCD calculator that can take unlimited amount of numbers,
and shows the steps (For example, you can do GCD(x, y, z, ...)). 
The method used is by finding the prime roots of the number, and find the 
maximum amount of each square root among the numbers.

———— I N P U T ————————————————————————————————————————————————————————

Enter the numbers for GCD(x, y, z, ...). Divide them with comma. (CTRL+C to quit)"""
        + (
            "\n\n\033[31mInvalid input. Please enter integers only.\033[0m\n"
            if invalid
            else ""
        )
    )

    nums = [str(num) for num in input("x, y, z, ... = ").replace(" ", "").split(",")]

    # Check if all inputs are integers
    if not Utils.CHECK_INT_INPUT(*nums):
        Utils.CLEAR_TERMINAL()
        PROGRAM(invalid=True)
        return
    else:
        nums = list(map(int, nums))

    print(
        f"""\033[33mGCD({', '.join(map(str, nums))})\033[0m

———— S T E P S ————————————————————————————————————————————————————————

### SOLVING STEPS

(1) Find the prime factorization of each number.
"""
    )

    # Prime factorization
    factors_list = []
    factor_counts_list = []  # New list to store factor counts for each number
    for num in nums:
        factors = []
        while num % 2 == 0:
            factors.append(2)
            num //= 2
        for i in range(3, int(num**0.5) + 1, 2):
            while num % i == 0:
                factors.append(i)
                num //= i
        if num > 2:
            factors.append(num)
        factors_list.append(factors)

        # Count factors and add to factor_counts_list
        factor_counts = {}
        for factor in factors:
            if factor in factor_counts:
                factor_counts[factor] += 1
            else:
                factor_counts[factor] = 1
        factor_counts_list.append(factor_counts)

    # Print prime factorization with exponent notation
    for i, num in enumerate(nums):
        factor_counts = factor_counts_list[i]  # Use the corresponding factor counts
        if num == 1 or len(factor_counts) == 1:
            print(f"{num} = {num}\n")
        else:
            factor_str = " * ".join(
                [
                    f"{factor}^{count}" if count > 1 else str(factor)
                    for factor, count in factor_counts.items()
                ]
            )
            print(
                f"{num} =",
                " * ".join(map(str, factors_list[i])) + f"\n{num} = {factor_str}\n",
            )

    print(
        "(2) Find the minimum exponents among the common prime factorizations, \nand multiply them together."
    )

    # Get the base of the factors
    factors = reduce(lambda x, y: list(set(x) & set(y)), factors_list)

    # Make the GCD string
    gcd_str = f"\nGCD({', '.join(map(str, nums))})"

    # If there are no common factors
    if not factors:
        # Print GCD
        print(f"{gcd_str} = 1 (no common factors)")
        common_factor_value = 1

    else:
        # Make the common factor string
        common_factor_counts = {}
        for factor in factors:
            factor_counts = [
                factor_counts_list[i].get(factor, 0) for i in range(len(nums))
            ]  # Add a check to handle missing keys
            common_factor_counts[factor] = min(factor_counts)
        common_factor_str = " * ".join(
            [
                f"{factor}^{count}" if count > 1 else str(factor)
                for factor, count in common_factor_counts.items()
            ]
        )

        # GCD value
        common_factor_value = reduce(
            lambda x, y: x * y,
            [factor**count for factor, count in common_factor_counts.items()],
        )

        # Print GCD
        print(
            f"{gcd_str} = {common_factor_str}\n"
            + f"{' ' * len(gcd_str)}= {common_factor_value}"
        )

    print(
        f"""
\033[33m∴ Therefore, the GCD of the numbers is {common_factor_value}\033[0m.

———— E X T R A ————————————————————————————————————————————————————————

### EXTRA: CHECKING PAIRWISE PRIME
"""
    )

    # Check pairwise relatively prime
    pairwise_prime = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            gcd = math.gcd(nums[i], nums[j])
            if gcd == 1:
                print(f"GCD({nums[i]}, {nums[j]}) = 1 (pairwise relatively prime)")
                pairwise_prime.append(True)
            else:
                print(f"GCD({nums[i]}, {nums[j]}) = {gcd}")
                pairwise_prime.append(False)

    if False not in pairwise_prime:
        print("\n\033[33m∴ The numbers are pairwise relatively prime.\033[0m")
    else:
        print("\n\033[33m∴ The numbers are not pairwise relatively prime.\033[0m")

    exit = Utils.CONFIRM_EXIT()
    if exit:
        return
    else:
        PROGRAM()
