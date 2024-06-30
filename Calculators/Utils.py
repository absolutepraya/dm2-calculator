import sys, subprocess
from . import Modular_Exponentiation, Trial_Division, GCD, GCD_Euclidean
from . import GCD_Bezout, LCM, Polynomial_Congruence, CRT, Back_Subtitution


# Clear terminal
def CLEAR_TERMINAL():
    if sys.platform == "win32":
        subprocess.run("cls", shell=True)
    elif sys.platform == "linux" or sys.platform == "darwin":
        subprocess.run("clear", shell=True)


# Get calculator description
def GET_CALC_DESC(num):
    if num == "1":
        return Modular_Exponentiation.DESC()
    elif num == "2":
        return Trial_Division.DESC()
    elif num == "3":
        return GCD.DESC()
    elif num == "4":
        return GCD_Euclidean.DESC()
    elif num == "5":
        return GCD_Bezout.DESC()
    elif num == "6":
        return LCM.DESC()
    elif num == "7":
        return Polynomial_Congruence.DESC()
    elif num == "8":
        return CRT.DESC()
    elif num == "9":
        return Back_Subtitution.DESC()
    else:
        return False


# Confirmation before exiting calculator
def CONFIRM_EXIT():
    print('\nType in "a" to reset the calculator, or "q" to quit.')
    choice = input("Input: ")
    if choice.lower() == "q":
        return True
    elif choice.lower() == "a":
        CLEAR_TERMINAL()
        return False
    else:
        print("\n\033[31mInvalid input.\033[0m")
        return CONFIRM_EXIT()


# Integer input validation
def INPUT_INT(msg):
    num = input(msg)
    if not num.isdecimal():
        print("\n\033[31mPlease enter a valid integer.\033[0m")
        return
    return num


# Positive integer input validation
def INPUT_INT_POS(num, down_bound=0):
    if not num.isdecimal() or int(num) <= down_bound:
        print(
            f"\033[31mPlease enter a valid positive integer greater than {down_bound}.\033[0m"
        )
        return
    return num
