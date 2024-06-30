import sys, subprocess
import time


# Clear terminal
def CLEAR_TERMINAL():
    if sys.platform == "win32":
        subprocess.run("cls", shell=True)
    elif sys.platform == "linux" or sys.platform == "darwin":
        subprocess.run("clear", shell=True)


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


# Handle general calculation errors
def HANDLE_CALC_ERRORS(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyboardInterrupt, EOFError):
            print("\n\n\033[31mExiting...\033[0m")
            # Timeout 1 second before exiting
            time.sleep(1)
        except Exception as e:
            print(f"\n\n\033[31mError: {e}\nExiting...\033[0m")
            # Timeout 1 second before exiting
            time.sleep(1)
    return wrapper


# Check all input variables if they are integers
def CHECK_INT_INPUT(*args):
    for arg in args:
        if not arg.isdecimal():
            return False
    return True
