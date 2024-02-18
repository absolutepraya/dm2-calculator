# Made by absolutepraya

from Calculators import Utils
from Calculators import Modular_Exponentiation, Trial_Division, GCD, GCD_Euclidean
from Calculators import GCD_Bezout, LCM, Polynomial_Congruence, CRT, Back_Subtitution

# Header
def header(extra="Enter a calculator number or command."):
    print("""\033[32m╒═══════════════════════════╕
  ┳┓┳┳┓┏┓  ┏┓  ┓   ┓       
  ┃┃┃┃┃┏┛  ┃ ┏┓┃┏┓┏┃┏┓╋┏┓┏┓  
  ┻┛┛ ┗┗━  ┗┛┗┻┗┗┗┻┗┗┻┗┗┛┛    by absolutepraya
╘═══════════════════════════╛

\033[34mEquipped with steps!\033[0m

>>> Available calculators:
1. Modular Exponentiation
2. Trial Division
3. GCD with Pairwise Prime
4. GCD Euclidean's Algorithm
5. GCD Benzout's Theorem
6. LCM (unlimited amount of numbers can be calculated)
7. Polynomial Congruence
8. Chinese Remainder Theorem (CRT)
9. Back Substitution

>>> Available commands:
- "h <calculator number>" or "help <calculator number>"
   ↪ Show the brief description of the calculator
- "q" or "quit"
   ↪ Quit the program

———— INPUT ————————————————————————————————————————————————————————

""" + extra)

invalid_count = 0
desc = ""

# Main
def main():
    global invalid_count, desc

    while True:
        Utils.CLEAR_TERMINAL()

        if invalid_count == 0 and desc:
            header(f"""\033[34mDesc:\033[0m
{desc} 

Enter a calculator number or command.""")
        elif invalid_count == 0 and not desc:
            header()
        else:
            header("""\033[31mPlease enter a valid input.\033[0m

Enter a calculator number or command.""")
    
        # Input
        choice = input("Input: ").lower().strip()
        print()

        if choice == "q" or choice.lower() == "quit":
            print("\033[34mGoodbye!\033[0m")
            break

        elif choice.startswith("h") or choice.startswith("help"):
            choice_list = choice.split()

            if len(choice_list) != 2: # Invalid input
                invalid_count += 1
                continue

            desc = Utils.GET_CALC_DESC(choice_list[1])

            if desc:
                invalid_count = 0
            else: # Invalid input
                invalid_count += 1
            continue

        else:
            invalid_count = 0
            desc = ""

            if choice == "1":
                Utils.CLEAR_TERMINAL()
                Modular_Exponentiation.PROGRAM()
            elif choice == "2":
                Utils.CLEAR_TERMINAL()
                Trial_Division.PROGRAM()
            elif choice == "3":
                Utils.CLEAR_TERMINAL()
                GCD.PROGRAM()
            elif choice == "4":
                Utils.CLEAR_TERMINAL()
                GCD_Euclidean.PROGRAM()
            elif choice == "5":
                Utils.CLEAR_TERMINAL()
                GCD_Bezout.PROGRAM()
            elif choice == "6":
                Utils.CLEAR_TERMINAL()
                LCM.PROGRAM()
            elif choice == "7":
                Utils.CLEAR_TERMINAL()
                Polynomial_Congruence.PROGRAM()
            elif choice == "8":
                Utils.CLEAR_TERMINAL()
                CRT.PROGRAM()
            elif choice == "9":
                Utils.CLEAR_TERMINAL()
                Back_Subtitution.PROGRAM()
            else:
                invalid_count += 1
                continue

if __name__ == "__main__":
    main()