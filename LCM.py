# Version: 1.20

import sys
from functools import reduce

print("""\033[32m┓ ┏┓┳┳┓
┃ ┃ ┃┃┃
┗┛┗┛┛ ┗  by absolutepraya\033[0m

LCM calculator that can take unlimited amount of numbers,
and shows the steps. For example, you can do LCM(x, y, z, ...).

———— I N P U T ————————————————————————————————————————————————————————

Enter the numbers for LCM(x, y, z, ...). Divide them with comma.""")

# Command line arguments
if len(sys.argv) > 1:
    nums = [int(num) for num in sys.argv[1:]]
# Input inside the program
else:
    nums = [int(num) for num in input("x, y, z, ... = ").split(",")]
print(f"""\033[33mLCM({', '.join(map(str, nums))})\033[0m

———— S T E P S ————————————————————————————————————————————————————————

### SOLVING STEPS

(1) Find the prime factorization of each number.
""")

# Prime factorization
factors_list = []
factor_counts_list = [] # New list to store factor counts for each number
for num in nums:
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    for i in range(3, int(num ** 0.5) + 1, 2):
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
    factor_counts = factor_counts_list[i] # Use the corresponding factor counts
    if num == 1 or len(factor_counts) == 1:
        print(f"{num} = {num}\n")
    else:
        factor_str = " * ".join([f"{factor}^{count}" if count > 1 else str(factor) for factor, count in factor_counts.items()])
        print(f"{num} =", " * ".join(map(str, factors_list[i])) + f"\n{num} = {factor_str}\n")

print("(2) Find the maximum exponents among the common prime factorizations, \nand multiply them together.")

# Get the base of the factors
factors = reduce(lambda x, y: list(set(x) | set(y)), factors_list)

# Make the LCM string
lcm_str = f"\nLCM({', '.join(map(str, nums))})"

# Make the common factor string
common_factor_counts = {}
for factor in factors:
    factor_counts = [factor_counts_list[i].get(factor, 0) for i in range(len(nums))]
    common_factor_counts[factor] = max(factor_counts)
common_factor_str = " * ".join([f"{factor}^{count}" if count > 1 else str(factor) for factor, count in common_factor_counts.items()])

# LCM value
common_factor_value = reduce(lambda x, y: x * y, [factor ** count for factor, count in common_factor_counts.items()])

# Print LCM
print(f"{lcm_str} = {common_factor_str}\n" +
f"{' ' * len(lcm_str)}= {common_factor_value}" +
f"\n\n\033[33m∴ Therefore, the LCM of the numbers is {common_factor_value}.\033[0m")
