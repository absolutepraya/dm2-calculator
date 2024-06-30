# Check prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


# Prime factorization
def prime_factorization(nums):
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
    return factors_list, factor_counts_list


# Euclidean algorithm
def euclidean_algorithm(x, y):
    while y != 0:
        print(f"{x} = {y} * {x // y} + {x % y}")
        x, y = y, x % y
    return x
