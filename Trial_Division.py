# Version: 1.2

import math
import sys

print("""┏┳┓  •  ┓  ┳┓•  • •    
 ┃ ┏┓┓┏┓┃  ┃┃┓┓┏┓┏┓┏┓┏┓
 ┻ ┛ ┗┗┻┗  ┻┛┗┗┛┗┛┗┗┛┛┗  by absolutepraya

Provides steps to check if a number is prime using the trial 
division method. The number of tries is also shown.

————————————————————————————————————————————————————————————
""")

# Command line input
if len(sys.argv) > 1:
    num = int(sys.argv[1])
    print(f"Number =  {num}")
# Input inside the program
else:
    print("Enter a number.")
    num = int(input("Number = "))
print("""
————————————————————————————————————————————————————————————
""")

# Prime numbers list using Sieve of Eratosthenes algorithm
num_root = math.floor(num**0.5)
sieve = [True] * (num_root+1)
for x in range(2, int(num_root**0.5) + 1):
    if sieve[x]: sieve[2*x::x] = [False] * len(sieve[2*x::x])
prime_lst =  [i for i in range(2, num_root+1) if sieve[i]]

# Result (1 of 2)
print(f"""### SOLVING STEPS:

(1) Find the square root of the number, then round it down.
x = ⌊√{num}⌋ = ⌊{num**0.5}⌋ = {num_root}

(2) Create a list of prime numbers from 2 to x.
Primes = {', '.join(map(str, prime_lst))}

(3) Check if the number is divisible by any of the prime numbers.""")

# Prime check
prime = True
tries = 0
for prime_num in prime_lst:
    tries += 1
    mod_res = num % prime_num
    if mod_res == 0:
        print(f"Try {tries}: {num} % {prime_num} = 0 ——> {prime_num} | {num} (divisible by {prime_num})")
        prime = False
        break
    else:
        print(f"Try {tries}: {num} % {prime_num} = {mod_res} —> {prime_num} ∤ {num} (not divisible)")

# Result (2 of 2)
print(f"""
Number of tries needed: {tries}
Maximum number of tries: {len(prime_lst)}
""")
if prime:
    print(f"""∴ {num} is a prime number.
  It's not divisible by any of the prime numbers from 2 to {num_root}.""")
else:
    print(f"∴ {num} is NOT a prime number, it's divisible by {prime_num}.")