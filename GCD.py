# Version: 1.1

import sys
import math
from functools import reduce

print("""┏┓              ┏┓┏┓┳┓
┃ ┏┓┏┳┓┏┳┓┏┓┏┓  ┃┓┃ ┃┃
┗┛┗┛┛┗┗┛┗┗┗┛┛┗  ┗┛┗┛┻┛  by absolutepraya

GCD calculator that can take unlimited amount of numbers, 
and shows the steps. For example, you can do GCD(x, y, z, ...).

————————————————————————————————————————————————————————————

Enter numbers for GCD(x, y, z, ...). Divide them with comma""")

# Command line arguments
if len(sys.argv) > 1:
    nums = [int(num) for num in sys.argv[1:]]
# Input inside the program
else:
    nums = [int(num) for num in input("x, y, z, ... = ").split(",")]
print(f"""GCD({', '.join(map(str, nums))})

————————————————————————————————————————————————————————————

### SOLVING STEPS

(1) Find the prime factorization of each number.
""")

# Prime factorization
factors_list = []
factor_counts_list = []  # New list to store factor counts for each number
for num in nums:
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
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

# GCD
factors = reduce(lambda x, y: list(set(x) & set(y)), factors_list)

# Print prime factorization with exponent notation
for i, num in enumerate(nums):
    factors = factors_list[i]
    factor_counts = factor_counts_list[i]  # Use the corresponding factor counts
    factor_str = " * ".join([f"{factor}^{count}" if count > 1 else str(factor) for factor, count in factor_counts.items()])
    print(f"{num} =", " * ".join(map(str, factors_list[i])) + f"\n{num} = {factor_str}\n")

print("(2) Find the common factors among the prime factorizations, \nand multiply them together.")

# Print common factors
common_factors = list(set(factors))
common_factor_counts = {}
for factor in common_factors:
    common_factor_counts[factor] = min(factor_counts.get(factor, 0) for factor_counts in factor_counts_list)
common_factor_str = " * ".join([f"{factor}^{count}" if count > 1 else str(factor) for factor, count in common_factor_counts.items()]) if common_factor_counts else "1"
common_factor_value = reduce(lambda x, y: x * y, [factor ** count for factor, count in common_factor_counts.items()])

# Print GCD
gcd_str = f"GCD({', '.join(map(str, nums))})"
if common_factor_value == 1:
    print(f"{gcd_str} = 1 (no common factors)")
else:
    print(f"{gcd_str} = {common_factor_str}")
    print(f"{' ' * len(gcd_str)} = {common_factor_value}")

print(f"\n∴ Therefore, the GCD of the numbers is {common_factor_value}.")
if common_factor_value == 1:
    print("  This means these numbers are pairwise relatively prime.")